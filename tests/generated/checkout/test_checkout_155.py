import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9241", "title": "Checkout scenario 9241", "data": {"sku": "SKU9241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9241@example.com", "threshold": 410}},
    {"id": "CHECKOUT-9242", "title": "Checkout scenario 9242", "data": {"sku": "SKU9242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9242@example.com", "threshold": 420}},
    {"id": "CHECKOUT-9243", "title": "Checkout scenario 9243", "data": {"sku": "SKU9243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9243@example.com", "threshold": 430}},
    {"id": "CHECKOUT-9244", "title": "Checkout scenario 9244", "data": {"sku": "SKU9244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9244@example.com", "threshold": 440}},
    {"id": "CHECKOUT-9245", "title": "Checkout scenario 9245", "data": {"sku": "SKU9245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9245@example.com", "threshold": 450}},
    {"id": "CHECKOUT-9246", "title": "Checkout scenario 9246", "data": {"sku": "SKU9246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9246@example.com", "threshold": 460}},
    {"id": "CHECKOUT-9247", "title": "Checkout scenario 9247", "data": {"sku": "SKU9247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9247@example.com", "threshold": 470}},
    {"id": "CHECKOUT-9248", "title": "Checkout scenario 9248", "data": {"sku": "SKU9248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9248@example.com", "threshold": 480}},
    {"id": "CHECKOUT-9249", "title": "Checkout scenario 9249", "data": {"sku": "SKU9249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9249@example.com", "threshold": 490}},
    {"id": "CHECKOUT-9250", "title": "Checkout scenario 9250", "data": {"sku": "SKU9250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9250@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
