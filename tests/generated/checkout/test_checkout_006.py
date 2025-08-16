import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0301", "title": "Checkout scenario 301", "data": {"sku": "SKU301", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user301@example.com", "threshold": 10}},
    {"id": "CHECKOUT-0302", "title": "Checkout scenario 302", "data": {"sku": "SKU302", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user302@example.com", "threshold": 20}},
    {"id": "CHECKOUT-0303", "title": "Checkout scenario 303", "data": {"sku": "SKU303", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user303@example.com", "threshold": 30}},
    {"id": "CHECKOUT-0304", "title": "Checkout scenario 304", "data": {"sku": "SKU304", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user304@example.com", "threshold": 40}},
    {"id": "CHECKOUT-0305", "title": "Checkout scenario 305", "data": {"sku": "SKU305", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user305@example.com", "threshold": 50}},
    {"id": "CHECKOUT-0306", "title": "Checkout scenario 306", "data": {"sku": "SKU306", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user306@example.com", "threshold": 60}},
    {"id": "CHECKOUT-0307", "title": "Checkout scenario 307", "data": {"sku": "SKU307", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user307@example.com", "threshold": 70}},
    {"id": "CHECKOUT-0308", "title": "Checkout scenario 308", "data": {"sku": "SKU308", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user308@example.com", "threshold": 80}},
    {"id": "CHECKOUT-0309", "title": "Checkout scenario 309", "data": {"sku": "SKU309", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user309@example.com", "threshold": 90}},
    {"id": "CHECKOUT-0310", "title": "Checkout scenario 310", "data": {"sku": "SKU310", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user310@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
