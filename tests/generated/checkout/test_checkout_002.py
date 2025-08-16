import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0061", "title": "Checkout scenario 61", "data": {"sku": "SKU61", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user61@example.com", "threshold": 610}},
    {"id": "CHECKOUT-0062", "title": "Checkout scenario 62", "data": {"sku": "SKU62", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user62@example.com", "threshold": 620}},
    {"id": "CHECKOUT-0063", "title": "Checkout scenario 63", "data": {"sku": "SKU63", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user63@example.com", "threshold": 630}},
    {"id": "CHECKOUT-0064", "title": "Checkout scenario 64", "data": {"sku": "SKU64", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user64@example.com", "threshold": 640}},
    {"id": "CHECKOUT-0065", "title": "Checkout scenario 65", "data": {"sku": "SKU65", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user65@example.com", "threshold": 650}},
    {"id": "CHECKOUT-0066", "title": "Checkout scenario 66", "data": {"sku": "SKU66", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user66@example.com", "threshold": 660}},
    {"id": "CHECKOUT-0067", "title": "Checkout scenario 67", "data": {"sku": "SKU67", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user67@example.com", "threshold": 670}},
    {"id": "CHECKOUT-0068", "title": "Checkout scenario 68", "data": {"sku": "SKU68", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user68@example.com", "threshold": 680}},
    {"id": "CHECKOUT-0069", "title": "Checkout scenario 69", "data": {"sku": "SKU69", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user69@example.com", "threshold": 690}},
    {"id": "CHECKOUT-0070", "title": "Checkout scenario 70", "data": {"sku": "SKU70", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user70@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
