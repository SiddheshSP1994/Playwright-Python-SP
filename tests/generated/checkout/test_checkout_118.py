import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7021", "title": "Checkout scenario 7021", "data": {"sku": "SKU7021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7021@example.com", "threshold": 210}},
    {"id": "CHECKOUT-7022", "title": "Checkout scenario 7022", "data": {"sku": "SKU7022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7022@example.com", "threshold": 220}},
    {"id": "CHECKOUT-7023", "title": "Checkout scenario 7023", "data": {"sku": "SKU7023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7023@example.com", "threshold": 230}},
    {"id": "CHECKOUT-7024", "title": "Checkout scenario 7024", "data": {"sku": "SKU7024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7024@example.com", "threshold": 240}},
    {"id": "CHECKOUT-7025", "title": "Checkout scenario 7025", "data": {"sku": "SKU7025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7025@example.com", "threshold": 250}},
    {"id": "CHECKOUT-7026", "title": "Checkout scenario 7026", "data": {"sku": "SKU7026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7026@example.com", "threshold": 260}},
    {"id": "CHECKOUT-7027", "title": "Checkout scenario 7027", "data": {"sku": "SKU7027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7027@example.com", "threshold": 270}},
    {"id": "CHECKOUT-7028", "title": "Checkout scenario 7028", "data": {"sku": "SKU7028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7028@example.com", "threshold": 280}},
    {"id": "CHECKOUT-7029", "title": "Checkout scenario 7029", "data": {"sku": "SKU7029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7029@example.com", "threshold": 290}},
    {"id": "CHECKOUT-7030", "title": "Checkout scenario 7030", "data": {"sku": "SKU7030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7030@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
