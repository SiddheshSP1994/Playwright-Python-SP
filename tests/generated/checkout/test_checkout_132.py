import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7861", "title": "Checkout scenario 7861", "data": {"sku": "SKU7861", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7861@example.com", "threshold": 610}},
    {"id": "CHECKOUT-7862", "title": "Checkout scenario 7862", "data": {"sku": "SKU7862", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7862@example.com", "threshold": 620}},
    {"id": "CHECKOUT-7863", "title": "Checkout scenario 7863", "data": {"sku": "SKU7863", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7863@example.com", "threshold": 630}},
    {"id": "CHECKOUT-7864", "title": "Checkout scenario 7864", "data": {"sku": "SKU7864", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7864@example.com", "threshold": 640}},
    {"id": "CHECKOUT-7865", "title": "Checkout scenario 7865", "data": {"sku": "SKU7865", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7865@example.com", "threshold": 650}},
    {"id": "CHECKOUT-7866", "title": "Checkout scenario 7866", "data": {"sku": "SKU7866", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7866@example.com", "threshold": 660}},
    {"id": "CHECKOUT-7867", "title": "Checkout scenario 7867", "data": {"sku": "SKU7867", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7867@example.com", "threshold": 670}},
    {"id": "CHECKOUT-7868", "title": "Checkout scenario 7868", "data": {"sku": "SKU7868", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7868@example.com", "threshold": 680}},
    {"id": "CHECKOUT-7869", "title": "Checkout scenario 7869", "data": {"sku": "SKU7869", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7869@example.com", "threshold": 690}},
    {"id": "CHECKOUT-7870", "title": "Checkout scenario 7870", "data": {"sku": "SKU7870", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7870@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
