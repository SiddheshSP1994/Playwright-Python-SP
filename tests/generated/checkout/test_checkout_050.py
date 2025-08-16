import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2941", "title": "Checkout scenario 2941", "data": {"sku": "SKU2941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2941@example.com", "threshold": 410}},
    {"id": "CHECKOUT-2942", "title": "Checkout scenario 2942", "data": {"sku": "SKU2942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2942@example.com", "threshold": 420}},
    {"id": "CHECKOUT-2943", "title": "Checkout scenario 2943", "data": {"sku": "SKU2943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2943@example.com", "threshold": 430}},
    {"id": "CHECKOUT-2944", "title": "Checkout scenario 2944", "data": {"sku": "SKU2944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2944@example.com", "threshold": 440}},
    {"id": "CHECKOUT-2945", "title": "Checkout scenario 2945", "data": {"sku": "SKU2945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2945@example.com", "threshold": 450}},
    {"id": "CHECKOUT-2946", "title": "Checkout scenario 2946", "data": {"sku": "SKU2946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2946@example.com", "threshold": 460}},
    {"id": "CHECKOUT-2947", "title": "Checkout scenario 2947", "data": {"sku": "SKU2947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2947@example.com", "threshold": 470}},
    {"id": "CHECKOUT-2948", "title": "Checkout scenario 2948", "data": {"sku": "SKU2948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2948@example.com", "threshold": 480}},
    {"id": "CHECKOUT-2949", "title": "Checkout scenario 2949", "data": {"sku": "SKU2949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2949@example.com", "threshold": 490}},
    {"id": "CHECKOUT-2950", "title": "Checkout scenario 2950", "data": {"sku": "SKU2950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2950@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
