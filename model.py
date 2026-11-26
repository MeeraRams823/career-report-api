from data import Jobs, Courses, Student_Profile

class IntegratedGCNAdvisor:
    """Placeholder for the proprietary advisor model. Returns a sample report."""

    def __init__(self, jobs: list[Jobs], courses: list[Courses], student_profile: Student_Profile):
        # Convert the Pydantic models to plain dicts
        self.jobs = [job.model_dump() for job in jobs]
        self.courses = [course.model_dump() for course in courses]
        self.student_profile = student_profile.model_dump() if student_profile else {}

        if not self.jobs or not self.courses:
            raise ValueError("jobs and courses must not be empty.")

    def run(self):
        # The real model generates a personalized report here.
        return "Sample Report"

# NOTE: The production model (a graph-based course/career advisor) was
# developed by a collaborator and is not included in this repository.
# This placeholder mirrors its interface so the API can run end to end.
# The API layer around it (data models, endpoint, deployment) is my work.
