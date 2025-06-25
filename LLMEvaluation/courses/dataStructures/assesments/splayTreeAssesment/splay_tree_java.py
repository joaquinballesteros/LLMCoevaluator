import os
from LLMEvaluation.courses.dataStructures.data_structures_general import (
    DataStucturesGeneral,
)
from LLMEvaluation.utils.llm_base import LLMBase
import shutil  # To copy the student's code into the project for compilation
import subprocess  # To execute Java compilation and execution commands


class SplayTreeJava(DataStucturesGeneral):
    llm = None

    def __init__(self):
        super().__init__()

    def specific_rubric(self):
        """
        Returns the specific rubric for SplayTree methods.
        """
        return """These are the methods to evaluate and provide formative feedback for. In a Splay tree, whenever a node is accessed (for deletion, modification, or reading), it must be moved to the root:
 - `void insert(K key)` (1 point): inserts a key into the tree. If the key already exists, replaces the existing node with the new key. Throws **EmptySearchTreeException** if `key` is null.
 - `K search(K key)` (1.5 points): searches for the key in the tree and returns it if present. If not found, returns null. Throws **EmptySearchTreeException** if `key` is null.
 - `void delete(K key)` (1 point): Deletes a key from the tree if present. Throws **EmptySearchTreeException** if `key` is null.
 - `void clear()` (1 point): Removes all elements from the tree, leaving it empty.
 - `void deleteMinimum()` (0.5 point): Removes the smallest key from the tree. Uses the *splay* method to move the minimum. Throws **EmptySearchTreeException** if the tree is empty.
 - `zigzigRight(Node<K> node)` (1 point): Performs a double right rotation given the grandparent (`Node<K> node`). After the first rotation, if the left child is NULL, does not perform the second, returning the node with only one rotation applied. The input node is always non-NULL.
 - `zigzigLeft(Node<K> node)` (1 point): Performs a double left rotation given the grandparent (`Node<K> node`). After the first rotation, if the right child is NULL, does not perform the second, returning the node with only one rotation applied. The input node is always non-NULL.
 - `zigzagRightLeft(Node<K> node)` (1 point): Performs a double rotation, first right then left, given the grandparent (`Node<K> node`). The first rotation **is not performed if there is no subtree on the left branch of the right child.** The input node is always non-NULL.
 - `zigzagLeftRight(Node<K> node)` (1 point): Performs a double rotation, first left then right, given the grandparent (`Node<K> node`). The first rotation **is not performed if there is no subtree on the right branch of the left child.** The input node is always non-NULL.
 - `copyOf(SearchTree<K> that)` (0.5 points): Copies the data.
 - `copyOf(SplayTree<K> that)` (0.5 points): Copies the data maintaining the same structure.

 The following methods are already implemented and should not be evaluated:
 private Node<K> rotateRight(Node<K> node)
 private Node<K> rotateLeft(Node<K> node)
 private Node<K> splay(Node<K> node, K key)
 private Node<K> zigLeft(Node<K> node)
 private Node<K> zigRight(Node<K> node)
 public K minimum()
  """

    def sample_output(self):
        """
        Returns a sample output of the evaluation in HTML format.
        """
        return """Final grade: 3/10<br>

<table border="1">
  <tr>
  <th>Method</th>
  <th>Score</th>
  <th>Feedback</th>
  </tr>
  <tr>
  <td>insert(K key)</td>
  <td>0/1</td>
  <td>**Functionality:** The method has functional errors. It uses `search(key) == key`, which compares references instead of value equality, preventing correct detection of duplicate keys. Also, the insertion logic inside the loop does not handle all cases properly, which could lead to incorrect insertions or orphan nodes. Carefully review edge cases (single node, empty tree, etc).
  **Clarity:** Unnecessary variables like `padre` are created and can be removed.
  **Maintainability:** Correct.
  **Efficiency:** The insertion algorithm's complexity is not optimal (you use the *splay* method multiple times).
  **Formative Suggestion:** Review how comparisons work in Java. Always test edge cases to ensure robustness.
  </td>
  </tr>
  <tr>
  <td>search(K key)</td>
  <td>0/1.5</td>
  <td>**Functionality:** The method does not correctly handle the case when the tree is empty, which may cause a `NullPointerException`. Also, it uses `search(key) == key`, which is incorrect as it compares references instead of value equality.
  **Clarity:** Variable names are descriptive, which is positive. Reduce nesting when possible. You can add the negated if condition to the loop and avoid having an if inside. Add comments to facilitate code understanding.
  **Maintainability:** The method is short and uses private method calls, which is positive. However, the complexity in the loop with a nested if makes future updates harder.
  **Efficiency:** No comments.
  **Formative Suggestion:** Always check that parameters work in all possible ranges to ensure your code works well.
  </td>
  </tr>
  <tr>
  <td>delete(K key)</td>
  <td>0/1</td>
  <td>**Functionality:** The method does not actually remove the key from the tree; you should set the node to null.
  **Clarity:** The control logic is insufficient for deletion; you should separate the search (call Splay and the node to delete becomes the root) from the deletion.
  **Maintainability:** No comments.
  **Efficiency:** No comments.
  **Formative Suggestion:** Use the debugger to see how your algorithm behaves step by step and detect these errors.
  </td>
  </tr>
  <tr>
  <td>clear()</td>
  <td>1/1</td>
  <td>**Functionality:** Correct implementation that removes all elements from the tree.
  **Clarity:** The flow is clear and linear, and variable names are descriptive.
  **Maintainability:** Code is easy to maintain and understand.
  **Efficiency:** Efficient in terms of time and space.
  **Formative Suggestion:** Good implementation! Clear and simple.
    </td>
  </tr>
  <tr>
  <td>deleteMinimum()</td>
  <td>0/0.5</td>
  <td>**Functionality:** The method does not correctly handle the case when the tree is empty, which should throw an `EmptySearchTreeException`.
  **Clarity:** Variable names should be more descriptive, and remember to use comments in more complex parts.
  **Maintainability:** Reuse and do not duplicate code. You already have a Minimum method to find the minimum and another delete method to remove it.
  **Efficiency:** The implementation is efficient, although the functionality is incorrect.
  **Formative Suggestion:** Whenever possible, reuse existing code to avoid unnecessary duplication.
  </td>
  </tr>
  <tr>
  <td>zigzigRight(Node&lt;K&gt; node)</td>
  <td>1/1</td>
  <td>**Functionality:** The double right rotation implementation is correct.
  **Clarity:** Variables `nodeToRotate` and `parent` do not make it easy to follow the rotations. Reuse the same variable for rotations and add comments to explain the process.
  **Maintainability:** Correct, the method is short and easy to maintain.
  **Efficiency:** Efficient in O(1) time.
  **Formative Suggestion:** Keep it up, good code, efficient and maintainable.</td>
  </td>
  </tr>
  <tr>
  <td>zigzigLeft(Node&lt;K&gt; node)</td>
  <td>1/1</td>
 <td>**Functionality:** Correct.
  **Clarity:** Use more descriptive and longer variable names, and add comments to explain the process in more complex parts.
  **Maintainability:** Correct.
  **Efficiency:** Efficient in O(1) time.
  **Formative Suggestion:** A clear, efficient, and maintainable solution.</td>
  </td>
  </tr>
  <tr>
  <td>zigzagRightLeft(Node&lt;K&gt; node)</td>
  <td>0/1</td>
  <td>**Functionality:** The double rotation in this method does not correctly handle all possible cases, especially when there is no subtree on the left branch of the right child.
  **Clarity:** Simplify conditions and document complex parts to facilitate code understanding.
  **Maintainability:** The implemented logic is complicated and error-prone; create private methods to help and facilitate future maintenance.
  **Efficiency:** No comments.
  **Formative Suggestion:** Review the rotation logic and ensure they are applied correctly to the right nodes. Use the debugger to see how your algorithm behaves step by step and detect these errors.
  </td>
  </tr>
  <tr>
  <td>zigzagLeftRight(Node&lt;K&gt; node)</td>
  <td>0/1</td>
  <td>**Functionality:** The left-right double rotation implementation does not properly handle all scenarios, especially when there is no subtree on the right branch of the left child.
  **Clarity:** Simplify conditions and avoid unnecessary variables, which complicate code readability.
  **Maintainability:** The implemented logic is complicated and error-prone; create private methods to help and facilitate future maintenance.
  **Efficiency:** No comments.
  **Formative Suggestion:** Review the rotation logic and ensure they are applied correctly to the right nodes. Use the debugger to see how your algorithm behaves step by step and detect these errors.
  </td>
  </tr>
  <tr>
  <td>copyOf(SearchTree&lt;K&gt; that)</td>
  <td>0/0.5</td>
  <td>**Functionality:** The method copies the data but does not maintain the original tree structure, which does not meet the requirement to maintain the same structure.
  **Clarity:** Descriptive names and clear execution flow.
  **Maintainability:** No comments.
  **Efficiency:** No comments.
  **Formative Suggestion:** Carefully review the class documentation and ensure the method meets the established requirements.
  </td>
  </tr>
  <tr>
  <td>copyOf(SplayTree&lt;K&gt; that)</td>
  <td>0/0.5</td>
  <td>**Functionality:** Similar to the previous method, it does not preserve the original tree structure, which is a requirement violation.
  **Clarity:** Descriptive names and appropriate comments.
  **Maintainability:** No comments.
  **Efficiency:** No comments.
  **Formative Suggestion:** Carefully review the class documentation and ensure the method meets the established requirements.
  </td>
  </tr>
</table>
  """

    def input_files(self, input_folder):
        """
        Returns a list of all Java files in the input_folder (recursively).
        """
        files = []
        for root, _, files_in_dir in os.walk(input_folder):
            for file in files_in_dir:
                if file.endswith(tuple(".java")):
                    full_path = os.path.join(root, file)
                    files.append(full_path)
        return files

    def build_project(self, input_folder):
        """
        Copies user Java files to the working directory, compiles the project using Maven,
        and returns the concatenated user code and the compilation output.
        """

        compilation_output = ""
        userCode = ""
        work_space_folder = os.path.dirname(os.path.abspath(__file__)) + "/workspace"
        main_path = (
            work_space_folder + "/src/main/java/org/uma/ed/datastructures/searchtree/"
        )
        try:
            input_files = self.input_files(input_folder)
            for input_file in input_files:
                os.makedirs(os.path.dirname(input_file), exist_ok=True)
                relative_path = os.path.relpath(input_file, input_folder)
                dest_path = os.path.join(main_path, relative_path)
                shutil.copy(input_file, dest_path)

            # Command to execute

            command = f"""mvn -f {work_space_folder} compile"""

            result = subprocess.run(command, shell=True, text=True, capture_output=True)

            compilation_output = (
                "Compiles with ERRORS."
                if "COMPILATION ERROR" in result.stdout
                else "Compiles successfully. "
            )

            # Read the contents of all the files in input_files and append to userCode
            for input_file in input_files:
                with open(input_file, "r") as f:
                    content = f.read()
                    userCode += content + "\n ------------------\n"
        except Exception as e:
            print("An error occurred while running the compilation command:", str(e))

        return userCode, compilation_output
