import file_manager
import pylint_analyzer
import performance_optimizer
import user_interface

def main():
    # Step 1: Get Python files to optimize
    python_files = file_manager.get_python_files()

    # Step 2: Analyze code using Pylint
    pylint_reports = pylint_analyzer.analyze_code(python_files)

    # Step 3: Perform optimizations based on Pylint suggestions
    optimized_code = performance_optimizer.optimize_performance(pylint_reports)

    # Step 4: Display results to the user
    user_interface.display_results(optimized_code)

    # Step 5: Write optimized code to new files
    write_optimized_code(optimized_code)

def write_optimized_code(optimized_code):
    for filename, code in optimized_code.items():
        new_filename = filename.replace('.py', '_optimized.py')
        with open(new_filename, 'w') as file:
            file.write(code)
        print(f"Optimized code written to: {new_filename}")

if __name__ == "__main__":
    main()
