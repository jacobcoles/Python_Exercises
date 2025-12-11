# Exercise Notebook Guidelines

## Purpose
These exercise notebooks are near-clones of the demo notebooks, with strategically removed code sections that participants must complete independently. The goal is meaningful practice, not trivial fill-in-the-blank.

## Design Principles

### 1. What to Remove (Code Gaps)

**Remove meaningful logic, not syntax:**
- Function/method names that require understanding (e.g., `.groupby()`, `.merge()`)
- Column names that require reading the data context
- Conditions and comparisons (e.g., `> 1000`, `== "EMEA"`)
- Aggregation choices (e.g., `"sum"`, `"mean"`)
- Parameters that require decision-making

**Keep visible:**
- Import statements (unless specifically teaching imports)
- Variable assignments structure
- Print statements and output formatting
- Comments explaining the task

### 2. Gap Difficulty Levels

**Level 1 - Single Element (Early notebooks, Day 1-2):**
```python
# Calculate the sum of prices
total = prices.___()  # Use sum method
```

**Level 2 - Multiple Elements (Mid course, Day 2-3):**
```python
# Filter for EMEA region
emea_sales = df[df[___] == ___]  # Column name and value
```

**Level 3 - Full Expression (Later notebooks, Day 3-4):**
```python
# Group by region and calculate total revenue
regional_totals = ___  # Use groupby, select column, aggregate
```

### 3. Progressive Complexity

| Day | Gap Style | Typical Removal |
|-----|-----------|-----------------|
| Day 1 | Single blanks | Method names, values |
| Day 2 | 2-3 blanks per line | Column names + methods |
| Day 3 | Partial expressions | Conditions, parameters |
| Day 4 | Full lines/blocks | Complete operations |

### 4. Context Requirements

**Each gap MUST have:**
- A comment explaining what the code should accomplish
- Enough surrounding context to understand the goal
- Reference to the method/approach in the comment (for beginners)

**Example of good context:**
```python
# Filter the DataFrame to keep only rows where Revenue exceeds 5000
# Use boolean filtering: df[df["column"] comparison value]
high_revenue = df[___]
```

### 5. What NOT to Remove

- Boilerplate/setup code (imports, data creation)
- Print statements that show expected output
- Variable names on the left side of assignments
- Comments that explain the task
- Code that would require memorization rather than understanding

### 6. Business User Considerations

- Keep data contexts relatable (sales, revenue, regions, products)
- Don't test obscure Python syntax
- Focus on Pandas operations they'll actually use
- Provide hints in comments using business terminology
- Reference the demo notebooks for complex operations

### 7. Pacing Guidelines

**Per notebook target:**
- 3-6 exercise gaps (not every cell needs a gap)
- Mix of difficulty levels within each notebook
- First gap should be achievable to build confidence
- Final gap can be more challenging

**Time estimate per notebook:**
- Day 1: 10-15 minutes each
- Day 2: 15-20 minutes each
- Day 3: 20-25 minutes each
- Day 4: 25-30 minutes each (except comprehensive which is longer)

### 8. Gap Notation

Use `___` with parenthetical hints:
```python
result = df.groupby(___)[___].___(___) # (group_column), (value_column), (aggregation), (function_list)
```

Or use numbered blanks for complex gaps:
```python
# (1) = column to group by
# (2) = column to aggregate
# (3) = aggregation function
result = df.groupby((1))[(2)].(3)()
```

### 9. Solution Availability

- Solutions remain in the original `course_notebooks/` folder
- Participants can reference demos if stuck
- Instructor circulates to provide hints
- Encourage trying before looking at solutions

### 10. Quality Checklist

Before finalizing each exercise notebook:
- [ ] All gaps have clear comments explaining the goal
- [ ] The notebook runs without errors when gaps are filled correctly
- [ ] Progressive difficulty within the notebook
- [ ] Business-relevant examples maintained
- [ ] Not too many gaps (avoid fatigue)
- [ ] Not too few gaps (meaningful practice)
