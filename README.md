# 🚗 Lab: Testing the Autonomous Vehicle Speed Controller

You are part of the software team developing a **speed controller** for an autonomous car.
This controller automatically adjusts throttle and braking to maintain safe speeds under different road and traffic conditions.

Your task is to:

1. **Design tests** using:
   * **Black-box testing** (based on input-output behavior)
   * **White-box testing** (based on internal logic)
   * **Category partition** and **boundary value analysis**
2. **Measure test coverage** and reason about test completeness.

## Functions Under Test

The functions under test (FUT) are implemented in the `speed_controller.py` module. The function `update_speed()` calculates the speed of the vehicle based on the speed limit, current road conditions, traffic density, and slope. See the [requiments specification](#-appendix-a---system-requirements-for-speedcontroller) for more details.

### Oracle - determining expected output

As you are creating test cases with a set of input values, you will need to determine what the expected output should be. You will need some sort of oracle to determine the correct output.

We have learned in class that an **oracle** in software testing is a mechanism used to determine whether a FUT has produced the correct output for a given input. It serves as a source of truth or a standard against which the actual output of the software is compared.

There are various mechanisms to determine the expected output ranging from expert inputs to comparing it to a reference system. For this exercise, you have two options to determine what the expected output value should be for a specific set of input values:

* **Requirements**: the [requiments specification](#-appendix-a---system-requirements-for-speedcontroller) describes the expected behavior of the FUT. You can follow the description of the input values and their impact on the output to determine what the expected output should be.
* **Legacy system**: the `legacy_speed_controller.py` module mimics a legacy system. You can use it to generate the expected output value for a given set of input values.

---

## 🐥 Step 1 — Run your first test

Take a look around. You'll find the Function Under Test (FUT) `update_speed()` in the `speed_controller.py` module. That is the function for which you will be creating unit tests. More specifically, you will be writing test cases that call the FUT with different input parameters and assert the outcome of running that function.

You'll also find a test module `test_black_box.py`. It uses the built-in Pyhton `unittest` framework to run the tests. A simple test case has been implemented to illustrate how to implement test cases. It contains a simple test case that specified input values, expected output value, and executes the FUT. It then defines an assertion that compares the actual result with the expected result.  You can run that test using the following command:

```bash
python -m unittest test_black_box.py
```

It will provide an output that indicates how many tests have been run and how many have failed.

🤔 Do you see any test failures? If so, what do you have to do to fix that issue?

---

## 🔍 Step 2 — Analyze Inputs Using Category Partition

The following exercise ask you to generate a list of input values for each parameter described above. You will do so using a combination of black box and white box approaches. Each task will be specific about what input parameter you should be generating input values for and which approach to use. Once you have identified input values for all parameters, you will write test cases with these values.

In class, we learned that we need to identify categories by how they affect the output or behavior of the application. What are the categories for each of the parameters? What are example values in each category? For example, a categorization for a fictional parameter `temperature` could be as follows:

* `cold` (`temperature < 30`): 0, 10
* `mild` (`30 <= temperature <= 60`): 32, 49
* `warm` (`temperature > 60`): 70, 80

🎯 For this task, consider the description provided for the input parameters `safety_mode` and `road_condition`. Apply the category partition method based on the parameter descriptions provided above.

---

## 🧮 Step 3 — Derive Boundary Values

Boundary value analysis tries to find issues around the boundaries of the value space. In class we have learned about two types of boundary values:

* **Nominal boundary values**: boundary values that are valid in the context of the requirements (e.g., `min+`, `max-`)
* **Invalid boundary values**: boundary values that are outside the specific range for that parameter (e.g., `min-`, `max+`)

Use the boundary value analysis method to identify test inputs for the parameters `traffic_density` and `slope_angle`. Follow the instructions provided in class. Separate nominal values from the invalid values. When you write your test cases, you can only have one invalid parameter value for each test case.

---

## ⚫ Step 4 — Write black box tests

After the above exercise, you should have input values for each of the parameters that influence the behavior of the `update_speed()` function. You will now develop the test cases based on these input values.

### Create test case spreadsheet

First, create test cases in a spreadsheet. Create a spreadsheet in which the top row lists the parameters as shown below. Then, list the values for each parameter in the rows below. For now, only list the *nominal* values from the boundary value analysis.

You will also have to determine the output value for each test case. In practice, there are various ways of determining the expected output (e.g., requirements, SMEs, etc. - see class slides). For this task, you can take a look at the source code to determine what you believe the output value should be.

| speed_limit | safety_mode | road_condition | traffic_density | slope_angle | outcome |
|-------------|-------------|----------------|-----------------|-------------|---------|
| 60          | true        | clear          | 12              | -2          | 62      |
| 60          | true        | wet            | 44              | -2          | 58      |
| 60          | true        | icy            | 78              | 9           | 55      |
| ...         | ...         | ...            | ...             | ...         | ...     |

For now, we will ignore interactions between parameters. That means you do not need to generate permutations between values of different parameters.

### Implement test cases

Next, open `test_black_box.py` and implement `10` of the tests that you identified. Use the example test to guide you in implementing your tests. In each test, you will define input values, invoke the FUT, and then assert the expected output.

🤔 What bugs did you find, if any? If you did find bugs, note them down and fix them before continuing.

---

## ⚪ Step 5 — White-Box Test Design

So far, you generated test cases based on requirements only. That is one approach to achieve a notion of coverage and gain confidence in your test cases. In this task, you will switch to a white-box testing approach. Study the program flow of `update_speed()` and devise test cases that achieve `100%` statement coverage. Create a new module named `test_white_box.py`. Then start implementing test cases that you have identified by studying the source code.

🤔 Did you find any more bugs? Again, write them down and fix them before continuing.

---

## 📊 Step 6 — Measure Test Coverage

In the previous tasks, you identified white box tests with the goal to achieve `100%` statement coverage. But you have not actually formally checked if you achieved that coverage. The `coverage` library can be used to generate a coverage report. If you have installed the dependencies in `requirements.txt`, you will be able to run the following commands:

```bash
coverage run -m unittest test_white_box.py
coverage report -m
```

Example output:

```bash
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
speed_controller.py      31     10    68%   15, 30, 32, 36, 42-45, 49, 51, 55
test_white_box.py         9      1    89%   12
---------------------------------------------------
TOTAL                    49     12    76%
```

If your test coverage is less than `100%`, modify your test cases until you achieve that goal. Use the `Missing` column to identify what statement has not been covered. Then add a test case that covers that statement.

## 🏁 Appendix A - System Requirements for SpeedController

### Overview

The `SpeedController` module is responsible for determining the appropriate target speed for an autonomous vehicle under varying environmental and operational conditions. It ensures that the vehicle operates within safe limits while adapting to road conditions, traffic density, and terrain slope. The controller also supports a safety mode for stricter speed enforcement.

### Functional Requirements

#### Initialization

* The system shall allow configuration of a maximum speed limit (`speed_limit`) at initialization. If not provided, the default shall be 60 km/h.
* The controller shall maintain the current speed internally and update it whenever conditions change.

#### Safety Mode

* The system shall provide a method to enable or disable safety mode.
* When safety mode is enabled, the target speed shall never exceed the maximum speed limit minus 10 km/h.
* When safety mode is disabled, the target speed shall not fall below zero.

#### Speed Adjustment Logic

The system shall compute a new target speed based on three factors: road condition, traffic density, and slope angle.

#### Road Condition

* The controller shall accept one of three valid road conditions: `clear`, `wet`, or `icy`.
* For `clear` roads, the base speed shall remain unchanged.
* For `wet` roads, the base speed shall be reduced by applying a multiplier of 0.85.
* For `icy` roads, the base speed shall be reduced by applying a multiplier of 0.6.
* If an invalid road condition is provided, the system shall raise an error.

#### Traffic Density

* The controller shall accept a traffic density value between 0 and 100.
* If traffic density is 50 or higher:
  * For values greater than 80, the base speed shall be reduced by 20 km/h.
  * For values between 50 and 80 inclusive, the base speed shall be reduced by 10 km/h.
* If traffic density is below 50, no adjustment shall be made.

#### Slope Angle

* The controller shall accept a slope angle between -10 and +10 degrees.
* Positive values indicate uphill; negative values indicate downhill.
* For uphill slopes, the base speed shall be reduced by the slope angle value.
* For downhill slopes, the base speed shall be increased by the absolute value of the slope angle.

### Output

After applying all adjustments, the controller shall return the new target speed rounded to two decimal places.

### Constraints

* Road condition must be one of the predefined values.
* Traffic density must be an integer between 0 and 100.
* Slope angle must be an integer between -10 and +10.

### Error Handling

* If any input parameter is outside its valid range or an invalid road condition is provided, the system shall raise a `ValueError`.

### Example Scenario

* Given a speed limit of 60 km/h, road condition `icy`, traffic density of 90, and slope angle of -5:
  * Base speed starts at 60.
  * Apply icy multiplier: 60 × 0.6 = 36.
  * Traffic density > 80: subtract 20 → 16.
  * Downhill slope: add 5 → 21.
  * afety mode enabled: clamp to 50 → final speed = 21.00 km/h.
