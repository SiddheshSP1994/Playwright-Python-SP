import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6121", "title": "Checkout scenario 6121", "data": {"sku": "SKU6121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6121@example.com", "threshold": 210}},
    {"id": "CHECKOUT-6122", "title": "Checkout scenario 6122", "data": {"sku": "SKU6122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6122@example.com", "threshold": 220}},
    {"id": "CHECKOUT-6123", "title": "Checkout scenario 6123", "data": {"sku": "SKU6123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6123@example.com", "threshold": 230}},
    {"id": "CHECKOUT-6124", "title": "Checkout scenario 6124", "data": {"sku": "SKU6124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6124@example.com", "threshold": 240}},
    {"id": "CHECKOUT-6125", "title": "Checkout scenario 6125", "data": {"sku": "SKU6125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6125@example.com", "threshold": 250}},
    {"id": "CHECKOUT-6126", "title": "Checkout scenario 6126", "data": {"sku": "SKU6126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6126@example.com", "threshold": 260}},
    {"id": "CHECKOUT-6127", "title": "Checkout scenario 6127", "data": {"sku": "SKU6127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6127@example.com", "threshold": 270}},
    {"id": "CHECKOUT-6128", "title": "Checkout scenario 6128", "data": {"sku": "SKU6128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6128@example.com", "threshold": 280}},
    {"id": "CHECKOUT-6129", "title": "Checkout scenario 6129", "data": {"sku": "SKU6129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6129@example.com", "threshold": 290}},
    {"id": "CHECKOUT-6130", "title": "Checkout scenario 6130", "data": {"sku": "SKU6130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6130@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
