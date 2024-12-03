#!/usr/bin/env python

import fileinput


def is_report_safe(report):
    ds = []
    for i in range(len(report) - 1):
        ds.append(report[i + 1] - report[i])

    if all(d > 0 for d in ds) or all(d < 0 for d in ds):
        if 1 <= max(abs(d) for d in ds) <= 3:
            return True

    return False


def is_report_safe_with_problem_dampener(report):
    sub_reports = []
    for i in range(len(report)):
        sub_report = report[:i] + report[i+1:]
        sub_reports.append(sub_report)
    return any(is_report_safe(r) for r in sub_reports)


def main():
    reports = []
    for line in fileinput.input():
        report = [int(x) for x in line.split()]
        reports.append(report)

    safe_reports = [report for report in reports if is_report_safe(report)]
    print(len(safe_reports))

    safe_reports_with_problem_dampener = [
        report
        for report in reports
        if is_report_safe_with_problem_dampener(report)
    ]
    print(len(safe_reports_with_problem_dampener))


if __name__ == "__main__":
    main()
