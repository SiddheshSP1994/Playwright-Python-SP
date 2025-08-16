import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0661", "title": "Checkout scenario 661", "data": {"sku": "SKU661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user661@example.com", "threshold": 610}},
    {"id": "CHECKOUT-0662", "title": "Checkout scenario 662", "data": {"sku": "SKU662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user662@example.com", "threshold": 620}},
    {"id": "CHECKOUT-0663", "title": "Checkout scenario 663", "data": {"sku": "SKU663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user663@example.com", "threshold": 630}},
    {"id": "CHECKOUT-0664", "title": "Checkout scenario 664", "data": {"sku": "SKU664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user664@example.com", "threshold": 640}},
    {"id": "CHECKOUT-0665", "title": "Checkout scenario 665", "data": {"sku": "SKU665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user665@example.com", "threshold": 650}},
    {"id": "CHECKOUT-0666", "title": "Checkout scenario 666", "data": {"sku": "SKU666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user666@example.com", "threshold": 660}},
    {"id": "CHECKOUT-0667", "title": "Checkout scenario 667", "data": {"sku": "SKU667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user667@example.com", "threshold": 670}},
    {"id": "CHECKOUT-0668", "title": "Checkout scenario 668", "data": {"sku": "SKU668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user668@example.com", "threshold": 680}},
    {"id": "CHECKOUT-0669", "title": "Checkout scenario 669", "data": {"sku": "SKU669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user669@example.com", "threshold": 690}},
    {"id": "CHECKOUT-0670", "title": "Checkout scenario 670", "data": {"sku": "SKU670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user670@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
