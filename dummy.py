from unittest.mock import patch

class A:
    val = 1

assert A.val == 1
with patch.object(A, "val", "patched_value"):
    print(A.val)
    assert A.val == "patched_value"

assert A.val == 1
