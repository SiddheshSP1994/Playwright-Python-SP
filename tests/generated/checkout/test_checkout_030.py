import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1741", "title": "Checkout scenario 1741", "data": {"sku": "SKU1741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1741@example.com", "threshold": 410}},
    {"id": "CHECKOUT-1742", "title": "Checkout scenario 1742", "data": {"sku": "SKU1742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1742@example.com", "threshold": 420}},
    {"id": "CHECKOUT-1743", "title": "Checkout scenario 1743", "data": {"sku": "SKU1743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1743@example.com", "threshold": 430}},
    {"id": "CHECKOUT-1744", "title": "Checkout scenario 1744", "data": {"sku": "SKU1744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1744@example.com", "threshold": 440}},
    {"id": "CHECKOUT-1745", "title": "Checkout scenario 1745", "data": {"sku": "SKU1745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1745@example.com", "threshold": 450}},
    {"id": "CHECKOUT-1746", "title": "Checkout scenario 1746", "data": {"sku": "SKU1746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1746@example.com", "threshold": 460}},
    {"id": "CHECKOUT-1747", "title": "Checkout scenario 1747", "data": {"sku": "SKU1747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1747@example.com", "threshold": 470}},
    {"id": "CHECKOUT-1748", "title": "Checkout scenario 1748", "data": {"sku": "SKU1748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1748@example.com", "threshold": 480}},
    {"id": "CHECKOUT-1749", "title": "Checkout scenario 1749", "data": {"sku": "SKU1749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1749@example.com", "threshold": 490}},
    {"id": "CHECKOUT-1750", "title": "Checkout scenario 1750", "data": {"sku": "SKU1750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1750@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
