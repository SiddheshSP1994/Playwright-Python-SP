import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0741", "title": "Orders scenario 741", "data": {"sku": "SKU741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user741@example.com", "threshold": 410}},
    {"id": "ORDERS-0742", "title": "Orders scenario 742", "data": {"sku": "SKU742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user742@example.com", "threshold": 420}},
    {"id": "ORDERS-0743", "title": "Orders scenario 743", "data": {"sku": "SKU743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user743@example.com", "threshold": 430}},
    {"id": "ORDERS-0744", "title": "Orders scenario 744", "data": {"sku": "SKU744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user744@example.com", "threshold": 440}},
    {"id": "ORDERS-0745", "title": "Orders scenario 745", "data": {"sku": "SKU745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user745@example.com", "threshold": 450}},
    {"id": "ORDERS-0746", "title": "Orders scenario 746", "data": {"sku": "SKU746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user746@example.com", "threshold": 460}},
    {"id": "ORDERS-0747", "title": "Orders scenario 747", "data": {"sku": "SKU747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user747@example.com", "threshold": 470}},
    {"id": "ORDERS-0748", "title": "Orders scenario 748", "data": {"sku": "SKU748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user748@example.com", "threshold": 480}},
    {"id": "ORDERS-0749", "title": "Orders scenario 749", "data": {"sku": "SKU749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user749@example.com", "threshold": 490}},
    {"id": "ORDERS-0750", "title": "Orders scenario 750", "data": {"sku": "SKU750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user750@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
