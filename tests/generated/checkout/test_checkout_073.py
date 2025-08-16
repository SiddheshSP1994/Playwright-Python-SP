import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4321", "title": "Checkout scenario 4321", "data": {"sku": "SKU4321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4321@example.com", "threshold": 210}},
    {"id": "CHECKOUT-4322", "title": "Checkout scenario 4322", "data": {"sku": "SKU4322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4322@example.com", "threshold": 220}},
    {"id": "CHECKOUT-4323", "title": "Checkout scenario 4323", "data": {"sku": "SKU4323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4323@example.com", "threshold": 230}},
    {"id": "CHECKOUT-4324", "title": "Checkout scenario 4324", "data": {"sku": "SKU4324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4324@example.com", "threshold": 240}},
    {"id": "CHECKOUT-4325", "title": "Checkout scenario 4325", "data": {"sku": "SKU4325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4325@example.com", "threshold": 250}},
    {"id": "CHECKOUT-4326", "title": "Checkout scenario 4326", "data": {"sku": "SKU4326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4326@example.com", "threshold": 260}},
    {"id": "CHECKOUT-4327", "title": "Checkout scenario 4327", "data": {"sku": "SKU4327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4327@example.com", "threshold": 270}},
    {"id": "CHECKOUT-4328", "title": "Checkout scenario 4328", "data": {"sku": "SKU4328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4328@example.com", "threshold": 280}},
    {"id": "CHECKOUT-4329", "title": "Checkout scenario 4329", "data": {"sku": "SKU4329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4329@example.com", "threshold": 290}},
    {"id": "CHECKOUT-4330", "title": "Checkout scenario 4330", "data": {"sku": "SKU4330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4330@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
