class InventoryAllocator:
    def __init__(self):
        pass

    @classmethod
    def fullyConsumed(self, order: dict) -> bool:
        for thing in order:
            if order[thing] != 0:
                return False
        return True

    def optimal_shipment(self, order: dict, warehouses: list) -> list:
        optimized_shipment = []
        for warehouse in warehouses:
            optimal_warehouse = {}
            for thing in order:
                if thing in warehouse['inventory']:
                    shipment_to_warehouse = min(order[thing], warehouse['inventory'][thing])
                    if shipment_to_warehouse != 0:
                        if warehouse['name'] in optimal_warehouse:
                            optimal_warehouse[warehouse['name']][thing] = shipment_to_warehouse
                        else:
                            optimal_warehouse[warehouse['name']] = {thing : shipment_to_warehouse}
                        order[thing] -= shipment_to_warehouse
            optimized_shipment.append(optimal_warehouse)
        if InventoryAllocator.fullyConsumed(order): return optimized_shipment
        return []

class InventoryAllocatorTest:
    inventory_allocator = InventoryAllocator()
    def empty_order_empty_optimized(self):
        print(
            'Empty Order:',
            self.inventory_allocator.optimal_shipment(   
                {}, 
                [
                    { 'name': 'owd', 'inventory': { 'apple': 5 }}, 
                    {}
                ]
            ) == [{}, {}]
        )
    def order_cannot_be_optimized(self):
        print(
            'Order that cannot be opimtized/fulfilled:',
            self.inventory_allocator.optimal_shipment(   
                {'apple': 3, }, 
                [
                    { 'name': 'owd', 'inventory': {'apple': 1, } }, 
                    { 'name': 'dm', 'inventory': {'apple': 1, 'banana': 2, } },
                    { 'name': 'sjc', 'inventory': {'orange': 3, } }
                ]
            ) == []
        )
    def split_shipment(self): 
        print(
            'Split order across multiple warehouses:',
            self.inventory_allocator.optimal_shipment(   
                { 'apple': 10 }, 
                [
                    { 'name': 'owd', 'inventory': { 'apple': 5 }}, 
                    { 'name': 'dm', 'inventory': { 'apple': 5 }}
                ]
            ) == [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        )
    def different_thing_types_with_seperate_warehouse_allocation(self):
        print(
            'Different thing types with allocation across seperate warehouses:',
            self.inventory_allocator.optimal_shipment(   
                { 'apple': 15, 'kiwi': 5, 'plum': 5 }, 
                [
                    { 'name': 'owd', 'inventory': {'banana': 5, 'kiwi': 10, 'pear': 20, 'apple': 10} }, 
                    { 'name': 'dm', 'inventory': {'apple': 5, 'plum': 20,} }
                ]
            ) == [{'owd': {'apple': 10, 'kiwi': 5}}, {'dm': {'apple': 5, 'plum': 5}}]
        )
    def order_gets_completed_by_closest_warehouse(self):
        print(
            'Order gets allocated to cheapest warehouses:',
            self.inventory_allocator.optimal_shipment(   
                {'apple': 3, }, 
                [
                    { 'name': 'owd', 'inventory': {'apple': 2, } }, 
                    { 'name': 'dm', 'inventory': {'apple': 4, 'banana': 2, } },
                    { 'name': 'sjc', 'inventory': {'orange': 3, } }
                ]
            ) == [{'owd': {'apple': 2}}, {'dm': {'apple': 1}}, {}]
        )
    def order_gets_completed_by_single_warehouse(self):
        print(
            'Order gets allocated a single warehouse:',
                self.inventory_allocator.optimal_shipment(   
                {'apple': 3, }, 
                [
                    { 'name': 'owd', 'inventory': {'apple': 4, } }, 
                    { 'name': 'sjc', 'inventory': {'orange': 3, } }
                ]
            )
        ) 

tests = InventoryAllocatorTest()
tests.empty_order_empty_optimized()
tests.order_cannot_be_optimized()
tests.split_shipment()
tests.order_cannot_be_optimized()
tests.different_thing_types_with_seperate_warehouse_allocation()
tests.order_gets_completed_by_closest_warehouse()
