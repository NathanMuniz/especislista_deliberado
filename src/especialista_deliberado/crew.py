from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from dotenv import load_dotenv

load_dotenv()

@CrewBase
class EspecialistaDeliberado():
	"""EspecialistaDeliberado crew"""


	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	
	@agent
	def expert(self) -> Agent:
		return Agent(
			config=self.agents_config['expert'],
			verbose=True
		)

	@agent
	def professor_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['professor_expert'],
			verbose=True
		)
	
	@agent
	def organiza_tarefaz(self) -> Agent:
		return Agent(
			config=self.agents_config['organiza_tarefaz'],
			verbose=True
		)

	@task
	def analisar_experts(self) -> Task:
		return Task(
			config=self.tasks_config['analisar_experts'],
		)

	@task
	def plano_estudos(self) -> Task:
		return Task(
			config=self.tasks_config['plano_estudos'],
		)
	
	@task
	def organiza_estudos(self) -> Task:
		return Task(
			config=self.tasks_config['organiza_estudos'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the EspecialistaDeliberado crew"""
		

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
