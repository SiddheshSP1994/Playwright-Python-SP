import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6961", "title": "Checkout scenario 6961", "data": {"sku": "SKU6961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6961@example.com", "threshold": 610}},
    {"id": "CHECKOUT-6962", "title": "Checkout scenario 6962", "data": {"sku": "SKU6962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6962@example.com", "threshold": 620}},
    {"id": "CHECKOUT-6963", "title": "Checkout scenario 6963", "data": {"sku": "SKU6963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6963@example.com", "threshold": 630}},
    {"id": "CHECKOUT-6964", "title": "Checkout scenario 6964", "data": {"sku": "SKU6964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6964@example.com", "threshold": 640}},
    {"id": "CHECKOUT-6965", "title": "Checkout scenario 6965", "data": {"sku": "SKU6965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6965@example.com", "threshold": 650}},
    {"id": "CHECKOUT-6966", "title": "Checkout scenario 6966", "data": {"sku": "SKU6966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6966@example.com", "threshold": 660}},
    {"id": "CHECKOUT-6967", "title": "Checkout scenario 6967", "data": {"sku": "SKU6967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6967@example.com", "threshold": 670}},
    {"id": "CHECKOUT-6968", "title": "Checkout scenario 6968", "data": {"sku": "SKU6968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6968@example.com", "threshold": 680}},
    {"id": "CHECKOUT-6969", "title": "Checkout scenario 6969", "data": {"sku": "SKU6969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6969@example.com", "threshold": 690}},
    {"id": "CHECKOUT-6970", "title": "Checkout scenario 6970", "data": {"sku": "SKU6970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6970@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
