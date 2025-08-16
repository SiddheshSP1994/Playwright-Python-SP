import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7981", "title": "Checkout scenario 7981", "data": {"sku": "SKU7981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7981@example.com", "threshold": 810}},
    {"id": "CHECKOUT-7982", "title": "Checkout scenario 7982", "data": {"sku": "SKU7982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7982@example.com", "threshold": 820}},
    {"id": "CHECKOUT-7983", "title": "Checkout scenario 7983", "data": {"sku": "SKU7983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7983@example.com", "threshold": 830}},
    {"id": "CHECKOUT-7984", "title": "Checkout scenario 7984", "data": {"sku": "SKU7984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7984@example.com", "threshold": 840}},
    {"id": "CHECKOUT-7985", "title": "Checkout scenario 7985", "data": {"sku": "SKU7985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7985@example.com", "threshold": 850}},
    {"id": "CHECKOUT-7986", "title": "Checkout scenario 7986", "data": {"sku": "SKU7986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7986@example.com", "threshold": 860}},
    {"id": "CHECKOUT-7987", "title": "Checkout scenario 7987", "data": {"sku": "SKU7987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7987@example.com", "threshold": 870}},
    {"id": "CHECKOUT-7988", "title": "Checkout scenario 7988", "data": {"sku": "SKU7988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7988@example.com", "threshold": 880}},
    {"id": "CHECKOUT-7989", "title": "Checkout scenario 7989", "data": {"sku": "SKU7989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7989@example.com", "threshold": 890}},
    {"id": "CHECKOUT-7990", "title": "Checkout scenario 7990", "data": {"sku": "SKU7990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7990@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
