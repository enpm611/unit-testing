

## 🚗 Lab: Testing the Autonomous Vehicle Speed Controller

### 🧭 Scenario

You are part of the software team developing a **speed controller** for an autonomous car.
This controller automatically adjusts throttle and braking to maintain safe speeds under different road and traffic conditions.

Your task is to:

1. **Design tests** using:
   * **Black-box testing** (based on input-output behavior)
   * **White-box testing** (based on internal logic)
   * **Category partition** and **boundary value analysis**
2. **Measure test coverage** and reason about test completeness.

### Functions Under Test

The functions under test (FUT) are implemented in the `speed_controller.py` module. 

---


## 🔍 Step 2 — Analyze Inputs Using Category Partition


The function `update_speed()` calculates the speed of the vehicle baseed on the speed limit, current road conditions, traffic density, and slope. The input parameters are defined as follows:

- `road_condition`: specifies if the road conditions are nominal or if there is a special condition that may impact how fast the vehicle should travel. This must be one of: `clear`, `wet`, or `icy` (as a string).
- `traffic_density`: based on traffic density, the speed will be increased or reduced. This value must be between `0` and `100`. If the traffic density is less than `50`, the speed is increased. Otherwise, the speed is reduced.
- `slope_angle`: specified the current degree of slope angle as a value between `-10` (downhill) and `+10` (uphill). The speed should be decreased if the vehicle is traveling downhill. It should be increased when traveling uphill.

In addition, the class `SpeedController` specifies a boolean flag `safety_value` that impact the execution of `update_speed()`. If that flag is set to `true`, the speed may never exceed `10mph` under the posted speed limit.



### Task 2a: Identify the categories for each of the parameters above

In class, we learned that we need to identify categories by how they affect the output or behavior of the application. What are the categories for each of the parameters? What are example values in each category? For example, a categorization for a fictional parameter `temperature` could be as follows:

- `cold` (`temperature < 30`): 0, 10, 25
- `mild` (`30 <= temperature <= 60`): 32, 49, 60
- `warm` (`temperature > 60`): 70, 80, 121

Apply the same approach to the parameters above.


### Task 2b: Interactions between parameters

Many bugs are found only if testing various interactions between parameter categories. For instance, given the `temperature` and combined with a boolean parameter `coat`, we could get the following permutations to test:


| temperature | coat  |
|-------------|-------|
| cold        | true  |
| cold        | false |
| mild        | true  |
| ...         | ...   |

What are the combinations of values to cover interactions between different categories of input values for `road_condition` and `safety_mode`?


---

## 🧮 Step 3 — Derive Boundary Values

Boundary value analysis tries to find issues around the boundaries of the value space. Apply boundary value analysis for `traffic_density` and `slope_angle`. The output should be a set of input values for each of these parameters.

---

## ⚫ Step 4 — Write black box tests

After the above exercise, you should have input values for each of the parameters. Now, write test cases that implement different test scenarios by drawing from those input parameters. Easiest is to create a table with test cases, such that each row has a value for a parameter and the expected return value:

| speed_limit | safety_mode | road_condition | traffic_density | slope_angle | outcome |
|-------------|-------------|----------------|-----------------|-------------|---------|
| 60          | true        | clear          | 12              | -2          | 62      |
| 60          | true        | wet            | 44              | -2          | 58      |
| 60          | true        | icy            | 78              | 9           | 55      |
| ...         | ...         | ...            | ...             | ...         | ...     |


Typically, you would generate permutations of all the different values. But for this exercise, just come up with some permutations that you feel would be useful for find bugs.

Next, open `test_black_box.py` and implement the tests that you identified. One test has already been implemented to illustrate how it works.

What bugs did you find, if any? If you did find bugs, note them down and fix them before continuing.

---

## ⚪ Step 5 — White-Box Test Design

Now switch to a white-box testing approach. Study the program flow of `update_speed()` and devise test cases that achieve 100% statement coverage.

Did you find any more bugs? Again, write them down and fix them before continuing.

---

## 📊 Step 6 — Measure Test Coverage

Python can generate a coverage report. Run the two commands below to first identify the coverage and then produce a report.

```bash
coverage run -m unittest discover
coverage report -m
```

Example output:

```
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
speed_controller.py      31     10    68%   15, 30, 32, 36, 42-45, 49, 51, 55
test_black_box.py         9      1    89%   12
test_white_box.py         9      1    89%   12
---------------------------------------------------
TOTAL                    49     12    76%
```

Modify your test cases until you achieve 100% statement coverage for `speed_controller.py`. Use the `Missing` column to identify what statement has not been covered. Then add a test case that covers that statement.
