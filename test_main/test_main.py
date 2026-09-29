import io
import sys
import unittest
from unittest.mock import patch

# Import functions from modules
from main import get_inputs, main
from src.display_performance import performance
from src.calculate_target_cgpa import calculate_target_cgpa, MAX_MARKS


class TestVITStudyMate(unittest.TestCase):

    @patch("builtins.input")
    def test_get_inputs_with_and_without_attendance_bonus(self, mock_input):
        """Test user input parsing, attendance bonus calculation, and capping at MAX_MARKS."""
        # Simulated input for 4 subjects:
        # 1: Attendance > 75% -> gets bonus (40 + 5 = 45)[cite: 3]
        # 2: Attendance <= 75% -> no bonus (40 + 0 = 40)[cite: 3]
        # 3: High score + attendance bonus capped at MAX_MARKS (48 + 5 = 53 -> capped at 50)[cite: 3]
        # 4: Regular scores (30 + 5 = 35)[cite: 3]
        mock_input.side_effect = [
            "Math", "40", "80",       # sub 1
            "Physics", "40", "75",    # sub 2
            "Chemistry", "48", "90",  # sub 3
            "English", "30", "85",    # sub 4
        ]

        subjects = get_inputs()

        self.assertEqual(len(subjects), 4)

        # Subject 1 (Bonus applied)
        self.assertEqual(subjects[0]["name"], "Math")
        self.assertEqual(subjects[0]["final_mark"], 45)
        self.assertEqual(subjects[0]["percentage"], 90.0)

        # Subject 2 (No bonus)
        self.assertEqual(subjects[1]["name"], "Physics")
        self.assertEqual(subjects[1]["final_mark"], 40)
        self.assertEqual(subjects[1]["percentage"], 80.0)

        # Subject 3 (Capped at 50)
        self.assertEqual(subjects[2]["name"], "Chemistry")
        self.assertEqual(subjects[2]["final_mark"], 50)
        self.assertEqual(subjects[2]["percentage"], 100.0)

        # Subject 4
        self.assertEqual(subjects[3]["name"], "English")
        self.assertEqual(subjects[3]["final_mark"], 35)
        self.assertEqual(subjects[3]["percentage"], 70.0)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_performance_calculation(self, mock_stdout):
        """Test display_performance calculation for average percentage and CGPA."""
        subjects = [
            {"name": "Math", "attendance": 80.0, "final_mark": 45.0, "percentage": 90.0},
            {"name": "Physics", "attendance": 70.0, "final_mark": 40.0, "percentage": 80.0},
            {"name": "Chemistry", "attendance": 90.0, "final_mark": 50.0, "percentage": 100.0},
            {"name": "English", "attendance": 85.0, "final_mark": 35.0, "percentage": 70.0},
        ]

        avg_pct, cgpa = performance(subjects)

        # Expected Avg: (90 + 80 + 100 + 70) / 4 = 85.0[cite: 2]
        # Expected CGPA: 85.0 / 10 = 8.5[cite: 2]
        self.assertAlmostEqual(avg_pct, 85.0)
        self.assertAlmostEqual(cgpa, 8.5)

    @patch("builtins.input", return_value="8.5")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_calculate_target_cgpa_achieved_or_higher(self, mock_stdout, mock_input):
        """Test target CGPA calculation when the user target is less than or equal to current CGPA."""
        subjects = [
            {"name": "Math", "final_mark": 45.0},
            {"name": "Physics", "final_mark": 40.0},
        ]
        # Current average is 85% (CGPA = 8.5)[cite: 1, 2]
        calculate_target_cgpa(subjects, current_avg_percentage=85.0)
        output = mock_stdout.getvalue()
        self.assertIn("You have already achieved your target CGPA!", output)

    @patch("builtins.input", return_value="8.0")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_calculate_target_cgpa_low_marks_improvement(self, mock_stdout, mock_input):
        """
        Test target CGPA module with low initial marks.
        
        Current performance: 
          - Math: 15/50 (30%)
          - Physics: 10/50 (20%)
          - Chemistry: 20/50 (40%)
          - English: 15/50 (30%)
          - Average percentage: 30% (Current CGPA: 3.0)
          
        Target CGPA: 8.0 (80% required)
          - Increment required: +50% (+25 marks per subject out of 50)
        """
        subjects = [
            {"name": "Math", "final_mark": 15.0},
            {"name": "Physics", "final_mark": 10.0},
            {"name": "Chemistry", "final_mark": 20.0},
            {"name": "English", "final_mark": 15.0},
        ]

        current_avg_pct = 30.0  # CGPA 3.0[cite: 2]
        calculate_target_cgpa(subjects, current_avg_pct)

        output = mock_stdout.getvalue()

        # Verify output table details[cite: 1]
        self.assertIn("TARGET CGPA ANALYSIS & REQUIRED MARKS", output)
        self.assertIn("Target CGPA:                                 8.00", output)
        self.assertIn("Required Overall Percentage:                80.00%", output)
        self.assertIn("Required Percentage Increment:             +50.00%", output)

        # Check required increase formatting for low score subjects (+25.00 marks each)[cite: 1]
        self.assertIn("Math                      | + 25.00 marks     | 40.00 / 50", output)
        self.assertIn("Physics                   | + 25.00 marks     | 35.00 / 50", output)
        self.assertIn("Chemistry                 | + 25.00 marks     | 45.00 / 50", output)
        self.assertIn("English                   | + 25.00 marks     | 40.00 / 50", output)

    @patch("builtins.input", return_value="9.0")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_calculate_target_cgpa_redistribution(self, mock_stdout, mock_input):
        """Test targeted CGPA calculation when excess target marks need redistribution across subjects."""
        # Current avg = 80% (CGPA 8.0). Target = 9.0 (Req. percentage = 90%, +10% increment = +5 marks out of 50)[cite: 1, 2]
        subjects = [
            {"name": "Math", "final_mark": 48.0},    # 48 + 5 = 53 -> capped at 50 (2 excess)[cite: 1]
            {"name": "Physics", "final_mark": 30.0}, # 30 + 5 + 2 (redistributed) = 37.0[cite: 1]
        ]

        calculate_target_cgpa(subjects, current_avg_percentage=80.0)
        output = mock_stdout.getvalue()

        self.assertIn("TARGET CGPA ANALYSIS & REQUIRED MARKS", output)
        self.assertIn("Physics", output)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_full_main_workflow(self, mock_stdout, mock_input):
        """Integration test for main workflow execution."""
        mock_input.side_effect = [
            "John Doe",             # Name
            "Math", "40", "80",     # Sub 1[cite: 3]
            "Physics", "35", "80",  # Sub 2[cite: 3]
            "Chemistry", "45", "80",# Sub 3[cite: 3]
            "English", "30", "80",  # Sub 4[cite: 3]
            "9.0"                   # Target CGPA[cite: 1]
        ]

        main()
        output = mock_stdout.getvalue()

        self.assertIn("WELCOME TO VIT-StudyMate John Doe", output)
        self.assertIn("CURRENT ACADEMIC PERFORMANCE", output)
        self.assertIn("TARGET CGPA ANALYSIS & REQUIRED MARKS", output)


if __name__ == "__main__":
    unittest.main()