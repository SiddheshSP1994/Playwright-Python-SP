import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4021", "title": "Checkout scenario 4021", "data": {"sku": "SKU4021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4021@example.com", "threshold": 210}},
    {"id": "CHECKOUT-4022", "title": "Checkout scenario 4022", "data": {"sku": "SKU4022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4022@example.com", "threshold": 220}},
    {"id": "CHECKOUT-4023", "title": "Checkout scenario 4023", "data": {"sku": "SKU4023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4023@example.com", "threshold": 230}},
    {"id": "CHECKOUT-4024", "title": "Checkout scenario 4024", "data": {"sku": "SKU4024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4024@example.com", "threshold": 240}},
    {"id": "CHECKOUT-4025", "title": "Checkout scenario 4025", "data": {"sku": "SKU4025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4025@example.com", "threshold": 250}},
    {"id": "CHECKOUT-4026", "title": "Checkout scenario 4026", "data": {"sku": "SKU4026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4026@example.com", "threshold": 260}},
    {"id": "CHECKOUT-4027", "title": "Checkout scenario 4027", "data": {"sku": "SKU4027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4027@example.com", "threshold": 270}},
    {"id": "CHECKOUT-4028", "title": "Checkout scenario 4028", "data": {"sku": "SKU4028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4028@example.com", "threshold": 280}},
    {"id": "CHECKOUT-4029", "title": "Checkout scenario 4029", "data": {"sku": "SKU4029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4029@example.com", "threshold": 290}},
    {"id": "CHECKOUT-4030", "title": "Checkout scenario 4030", "data": {"sku": "SKU4030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4030@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
