import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0961", "title": "Checkout scenario 961", "data": {"sku": "SKU961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user961@example.com", "threshold": 610}},
    {"id": "CHECKOUT-0962", "title": "Checkout scenario 962", "data": {"sku": "SKU962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user962@example.com", "threshold": 620}},
    {"id": "CHECKOUT-0963", "title": "Checkout scenario 963", "data": {"sku": "SKU963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user963@example.com", "threshold": 630}},
    {"id": "CHECKOUT-0964", "title": "Checkout scenario 964", "data": {"sku": "SKU964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user964@example.com", "threshold": 640}},
    {"id": "CHECKOUT-0965", "title": "Checkout scenario 965", "data": {"sku": "SKU965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user965@example.com", "threshold": 650}},
    {"id": "CHECKOUT-0966", "title": "Checkout scenario 966", "data": {"sku": "SKU966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user966@example.com", "threshold": 660}},
    {"id": "CHECKOUT-0967", "title": "Checkout scenario 967", "data": {"sku": "SKU967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user967@example.com", "threshold": 670}},
    {"id": "CHECKOUT-0968", "title": "Checkout scenario 968", "data": {"sku": "SKU968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user968@example.com", "threshold": 680}},
    {"id": "CHECKOUT-0969", "title": "Checkout scenario 969", "data": {"sku": "SKU969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user969@example.com", "threshold": 690}},
    {"id": "CHECKOUT-0970", "title": "Checkout scenario 970", "data": {"sku": "SKU970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user970@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
