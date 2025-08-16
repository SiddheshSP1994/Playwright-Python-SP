import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0941", "title": "Email scenario 941", "data": {"sku": "SKU941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user941@example.com", "threshold": 410}},
    {"id": "EMAIL-0942", "title": "Email scenario 942", "data": {"sku": "SKU942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user942@example.com", "threshold": 420}},
    {"id": "EMAIL-0943", "title": "Email scenario 943", "data": {"sku": "SKU943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user943@example.com", "threshold": 430}},
    {"id": "EMAIL-0944", "title": "Email scenario 944", "data": {"sku": "SKU944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user944@example.com", "threshold": 440}},
    {"id": "EMAIL-0945", "title": "Email scenario 945", "data": {"sku": "SKU945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user945@example.com", "threshold": 450}},
    {"id": "EMAIL-0946", "title": "Email scenario 946", "data": {"sku": "SKU946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user946@example.com", "threshold": 460}},
    {"id": "EMAIL-0947", "title": "Email scenario 947", "data": {"sku": "SKU947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user947@example.com", "threshold": 470}},
    {"id": "EMAIL-0948", "title": "Email scenario 948", "data": {"sku": "SKU948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user948@example.com", "threshold": 480}},
    {"id": "EMAIL-0949", "title": "Email scenario 949", "data": {"sku": "SKU949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user949@example.com", "threshold": 490}},
    {"id": "EMAIL-0950", "title": "Email scenario 950", "data": {"sku": "SKU950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user950@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
