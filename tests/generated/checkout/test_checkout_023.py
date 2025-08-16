import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1321", "title": "Checkout scenario 1321", "data": {"sku": "SKU1321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1321@example.com", "threshold": 210}},
    {"id": "CHECKOUT-1322", "title": "Checkout scenario 1322", "data": {"sku": "SKU1322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1322@example.com", "threshold": 220}},
    {"id": "CHECKOUT-1323", "title": "Checkout scenario 1323", "data": {"sku": "SKU1323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1323@example.com", "threshold": 230}},
    {"id": "CHECKOUT-1324", "title": "Checkout scenario 1324", "data": {"sku": "SKU1324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1324@example.com", "threshold": 240}},
    {"id": "CHECKOUT-1325", "title": "Checkout scenario 1325", "data": {"sku": "SKU1325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1325@example.com", "threshold": 250}},
    {"id": "CHECKOUT-1326", "title": "Checkout scenario 1326", "data": {"sku": "SKU1326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1326@example.com", "threshold": 260}},
    {"id": "CHECKOUT-1327", "title": "Checkout scenario 1327", "data": {"sku": "SKU1327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1327@example.com", "threshold": 270}},
    {"id": "CHECKOUT-1328", "title": "Checkout scenario 1328", "data": {"sku": "SKU1328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1328@example.com", "threshold": 280}},
    {"id": "CHECKOUT-1329", "title": "Checkout scenario 1329", "data": {"sku": "SKU1329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1329@example.com", "threshold": 290}},
    {"id": "CHECKOUT-1330", "title": "Checkout scenario 1330", "data": {"sku": "SKU1330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1330@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
