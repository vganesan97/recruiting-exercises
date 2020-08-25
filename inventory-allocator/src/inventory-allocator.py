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

inventory_allocator = InventoryAllocator()
print(
        inventory_allocator.optimal_shipment(   
        { 'apple': 10 }, 
        [
            { 'name': 'owd', 'inventory': { 'apple': 5 }}, 
            { 'name': 'dm', 'inventory': { 'apple': 5 }}
        ]
    )
)
print(
        inventory_allocator.optimal_shipment(   
        { 'apple': 5, 'banana': 5, 'orange': 5 }, 
        [
            { 'name': 'owd', 'inventory': {'banana': 5, 'orange': 10, 'pear': 20} }, 
            { 'name': 'dm', 'inventory': {'apple': 5, 'orange': 20,} }
        ]
    )
)
print(
        inventory_allocator.optimal_shipment(   
        {'apple': 3, }, 
        [
            { 'name': 'owd', 'inventory': {'apple': 2, } }, 
            { 'name': 'dm', 'inventory': {'apple': 4, 'banana': 2, } },
            { 'name': 'sjc', 'inventory': {'orange': 3, } }
        ]
    )
)   