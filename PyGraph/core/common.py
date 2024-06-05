def lerp(start, end, alpha):
    """执行一个线性插值

    >>> start + alpha * (end - start)

    :param start: start the value to interpolate from
    :param end: end the value to interpolate to
    :param alpha: alpha how far to interpolate
    :returns: The result of the linear interpolation
    """
    return start + alpha * (end - start)


def GetRangePct(MinValue, MaxValue, Value):
    """计算输入的值在从**MinValue**到**MaxValue**之间的百分比.

    :param MinValue: Minimum Value
    :param MaxValue: Maximum Value
    :param Value: Input value
    :returns: The percentage (from 0.0 to 1.0) between the two values
        where input value is
    """
    return (Value - MinValue) / (MaxValue - MinValue)
