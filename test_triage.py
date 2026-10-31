"""
Lab 10: The Priority Triage -- starter + verification (single file).

Complete insert, _sift_up, _sift_down, and extract_min below. Do not
modify anything below the "VERIFICATION SUITE" line.

Run: python test_triage.py
"""

import base64
import hashlib
import random
import sys
from typing import List

ASSIGNMENT_ID = "LAB10"


class MinHeap:
    """A binary min-heap backed by a flat Python list. Lower priority number = more critical."""

    def __init__(self) -> None:
        self._data: List[float] = []

    def __len__(self) -> int:
        return len(self._data)

    def insert(self, value: float) -> None:
        """Append value, then restore the heap property."""
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def _sift_up(self, index: int) -> None:
        """Recursively move a value upward until the heap property is restored."""
        # Base case: root has no parent
        if index == 0:
            return

        parent = (index - 1) // 2

        # Swap if child is smaller than parent
        if self._data[index] < self._data[parent]:
            self._data[index], self._data[parent] = (
                self._data[parent],
                self._data[index]
            )

            # Recursively continue upward
            self._sift_up(parent)

    def _sift_down(self, index: int) -> None:
        """Recursively move a value downward until the heap property is restored."""
        size = len(self._data)
        smallest = index

        left = 2 * index + 1
        right = 2 * index + 2

        # Find the smallest among parent and valid children
        if left < size and self._data[left] < self._data[smallest]:
            smallest = left

        if right < size and self._data[right] < self._data[smallest]:
            smallest = right

        # Base case: no child is smaller than the current node
        if smallest == index:
            return

        # Swap with the smallest child
        self._data[index], self._data[smallest] = (
            self._data[smallest],
            self._data[index]
        )

        # Recursively continue downward
        self._sift_down(smallest)

    def extract_min(self) -> float:
        """Remove and return the smallest value."""
        # Handle an empty heap
        if len(self._data) == 0:
            raise IndexError("extract_min from empty heap")

        # Save the minimum value
        minimum = self._data[0]

        # Handle a heap containing one element
        if len(self._data) == 1:
            self._data.pop()
            return minimum

        # Move the last element to the root
        self._data[0] = self._data.pop()

        # Restore the heap property
        self._sift_down(0)

        return minimum

# ============================== VERIFICATION SUITE ==============================
# Do not edit below this line.


def get_student_id() -> str:
    """Prompt for the student's USI username; baked into the Success Token
    so a copied/shared token decodes to someone else's name, not yours."""
    student_id = input("Enter your USI username (e.g. cwill): ").strip()
    while not student_id:
        student_id = input("Username cannot be blank. Enter your USI username: ").strip()
    return student_id


def generate_token(assignment_id: str, student_id: str) -> str:
    digest = hashlib.sha256(f"CS311-{assignment_id}-{student_id}-VERIFIED".encode()).hexdigest()[:16]
    raw = f"CS311|{assignment_id}|{student_id}|PASS|{digest}"
    return base64.b64encode(raw.encode()).decode()


def print_success_banner(assignment_id: str) -> None:
    student_id = get_student_id()
    token = generate_token(assignment_id, student_id)
    print("\n" + "=" * 60)
    print(f"  ALL CHECKS PASSED -- {assignment_id}")
    print(f"  STUDENT: {student_id}")
    print("  SUCCESS TOKEN (paste this into Blackboard):")
    print(f"  {token}")
    print("=" * 60 + "\n")


def check(label: str, condition: bool, failures: list) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}")
    if not condition:
        failures.append(label)


def is_heap_property(data: List[float]) -> bool:
    for i in range(len(data)):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(data) and data[left] < data[i]:
            return False
        if right < len(data) and data[right] < data[i]:
            return False
    return True


def main() -> int:
    failures: list = []

    print("Testing against the Part A, Q3 sequence: 5, 3, 8, 1, 9, 2...\n")
    heap = MinHeap()
    for v in [5, 3, 8, 1, 9, 2]:
        heap.insert(v)
        check(f"heap property holds after inserting {v}", is_heap_property(heap._data), failures)
    check("heap has 6 elements after 6 inserts", len(heap) == 6, failures)

    extracted = []
    while len(heap) > 0:
        m = heap.extract_min()
        extracted.append(m)
        check(f"heap property holds after extracting {m}", is_heap_property(heap._data), failures)
    check("extract_min pulls values out in fully sorted order", extracted == sorted([5, 3, 8, 1, 9, 2]), failures)

    print("\nTesting edge cases...\n")
    empty = MinHeap()
    try:
        empty.extract_min()
        check("extract_min on empty heap raises", False, failures)
    except (IndexError, ValueError):
        check("extract_min on empty heap raises IndexError/ValueError", True, failures)

    single = MinHeap()
    single.insert(42)
    check("extract_min on single-element heap returns that element", single.extract_min() == 42, failures)
    check("heap is empty after extracting its only element", len(single) == 0, failures)

    print("\nRandomized stress test (500 random priority values)...\n")
    rng = random.Random(311)
    values = [rng.randint(0, 100_000) for _ in range(500)]
    stress_heap = MinHeap()
    for v in values:
        stress_heap.insert(v)
    stress_extracted = [stress_heap.extract_min() for _ in range(len(values))]
    check("500-value stress test: extract_min order matches sorted order", stress_extracted == sorted(values), failures)

    print()
    if failures:
        print(f"{len(failures)} check(s) failed. No token issued.")
        return 1

    print_success_banner(ASSIGNMENT_ID)
    return 0


if __name__ == "__main__":
    sys.exit(main())
