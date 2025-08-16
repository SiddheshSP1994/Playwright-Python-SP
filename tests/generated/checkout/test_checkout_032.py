import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1861", "title": "Checkout scenario 1861", "data": {"sku": "SKU1861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1861@example.com", "threshold": 610}},
    {"id": "CHECKOUT-1862", "title": "Checkout scenario 1862", "data": {"sku": "SKU1862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1862@example.com", "threshold": 620}},
    {"id": "CHECKOUT-1863", "title": "Checkout scenario 1863", "data": {"sku": "SKU1863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1863@example.com", "threshold": 630}},
    {"id": "CHECKOUT-1864", "title": "Checkout scenario 1864", "data": {"sku": "SKU1864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1864@example.com", "threshold": 640}},
    {"id": "CHECKOUT-1865", "title": "Checkout scenario 1865", "data": {"sku": "SKU1865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1865@example.com", "threshold": 650}},
    {"id": "CHECKOUT-1866", "title": "Checkout scenario 1866", "data": {"sku": "SKU1866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1866@example.com", "threshold": 660}},
    {"id": "CHECKOUT-1867", "title": "Checkout scenario 1867", "data": {"sku": "SKU1867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1867@example.com", "threshold": 670}},
    {"id": "CHECKOUT-1868", "title": "Checkout scenario 1868", "data": {"sku": "SKU1868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1868@example.com", "threshold": 680}},
    {"id": "CHECKOUT-1869", "title": "Checkout scenario 1869", "data": {"sku": "SKU1869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1869@example.com", "threshold": 690}},
    {"id": "CHECKOUT-1870", "title": "Checkout scenario 1870", "data": {"sku": "SKU1870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1870@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
