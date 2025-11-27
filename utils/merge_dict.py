from typing import Callable


def merge_int_dicts(
    left: dict,
    right: dict,
    op: Callable[[int, int], int],
    *,
    default: int = 0,
    depth: int = 0,
    max_depth: int = 100,
) -> dict:
    """
    Gộp hai dictionary có thể chứa số nguyên hoặc dictionary lồng nhau,
    áp dụng một hàm tùy chỉnh lên các giá trị số nguyên và đệ quy xử lý
    các dictionary con.

    Hàm này được thiết kế để kết hợp hai cấu trúc dạng "cây" có cùng
    hình dạng. Tại mỗi khóa:

    - Nếu cả hai giá trị đều là số nguyên, hàm áp dụng phép toán
      `op(left_value, right_value)` và lưu kết quả.
    - Nếu cả hai giá trị đều là dictionary, hàm sẽ đệ quy gọi lại
      chính nó để gộp hai dictionary con.
    - Nếu một dictionary thiếu key, giá trị `default` sẽ được dùng
      thay thế (mặc định là 0).
    - Nếu gặp loại dữ liệu không phải số nguyên hoặc dictionary,
      hàm sẽ báo lỗi vì chỉ hỗ trợ hai loại dữ liệu này.

    Độ sâu đệ quy được giới hạn bởi `max_depth` để tránh vòng lặp vô hạn
    (ví dụ: do cấu trúc tham chiếu lẫn nhau hoặc độ sâu quá lớn).

    Parameters
    ----------
    left : dict
        Dictionary thứ nhất. Giá trị phải là số nguyên hoặc dictionary
        lồng nhau tuân theo cùng quy tắc.

    right : dict
        Dictionary thứ hai. Có yêu cầu cấu trúc giống với `left`.

    op : Callable[[int, int], int]
        Hàm dùng để kết hợp hai giá trị số nguyên. Ví dụ:
            - ``lambda a, b: a + b``  (cộng)
            - ``lambda a, b: max(a, b)`` (lấy giá trị lớn hơn)
            - ``lambda a, b: a - b`` (trừ)
        Hàm này chỉ được dùng khi cả hai giá trị tại khóa đều là số nguyên.

    default : int, optional
        Giá trị dùng khi một trong hai dictionary không chứa key đó.
        Vì phép toán chỉ áp dụng cho số nguyên, `default` phải là số nguyên.
        Mặc định là 0.

    depth : int, optional
        Tham số nội bộ để theo dõi độ sâu đệ quy hiện tại.
        Người dùng không cần chỉnh tham số này.
        Mặc định là 0.

    max_depth : int, optional
        Độ sâu đệ quy tối đa cho phép. Nếu quá giới hạn, hàm sẽ báo lỗi.
        Mặc định là 100.

    Returns
    -------
    dict
        Dictionary mới chứa kết quả đã được gộp từ `left` và `right`.
        Cấu trúc lồng nhau giữ nguyên, chỉ các giá trị số được kết hợp
        bằng hàm `op`.

    Raises
    ------
    ValueError
        - Nếu độ sâu đệ quy vượt quá `max_depth`.
        - Nếu gặp giá trị không phải số nguyên hoặc dictionary.
        - Nếu hàm không thể áp dụng toán tử trên hai kiểu dữ liệu không hợp lệ.

    Examples
    --------
    Ví dụ cơ bản với phép cộng:

    >>> merge_int_dicts(
    ...     {"a": 1, "b": {"x": 2}},
    ...     {"a": 3, "b": {"x": 5}},
    ...     op=lambda x, y: x + y
    ... )
    {'a': 4, 'b': {'x': 7}}

    Key chỉ tồn tại ở một bên:

    >>> merge_int_dicts({"a": 1}, {"b": 5}, op=lambda a, b: a + b)
    {'a': 1, 'b': 5}

    Dùng hàm tùy chỉnh (lấy giá trị lớn hơn):

    >>> merge_int_dicts(
    ...     {"a": 1, "b": {"n": 10}},
    ...     {"a": 3, "b": {"n": 7}},
    ...     op=max
    ... )
    {'a': 3, 'b': {'n': 10}}
    """
    if depth >= max_depth:
        raise ValueError(f"Maximum depth {max_depth} exceeded while merging dictionaries.")

    result = {}

    # Duyệt qua tất cả key có trong 1 trong 2 dict
    all_keys = set(left) | set(right)

    for key in all_keys:
        left_value = left.get(key, default)
        right_value = right.get(key, default)

        # Trường hợp cả hai giá trị đều là số nguyên
        if isinstance(left_value, int) and isinstance(right_value, int):
            result[key] = op(left_value, right_value)
            continue

        # Trường hợp cả hai đều là dict -> đệ quy
        if isinstance(left_value, dict) and isinstance(right_value, dict):
            result[key] = merge_int_dicts(
                left_value,
                right_value,
                op,
                default=default,
                depth=depth + 1,
                max_depth=max_depth,
            )
            continue

        # Nếu không phải int hoặc dict -> báo lỗi
        raise ValueError(
            f"Unsupported types for key '{key}': "
            f"{type(left_value)} and {type(right_value)}. "
            "Only int and dict values are supported."
        )

    return result

print(merge_int_dicts({"a": 1, "b": {"x": 2}},{"a": 3, "b": {"x": 5}},op=lambda x, y: x + y))
