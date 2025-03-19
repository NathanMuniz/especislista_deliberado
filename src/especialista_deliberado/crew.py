from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from dotenv import load_dotenv

load_dotenv()



@CrewBase
class Testcrew():
	"Uma equipe especialista nas informações da Bacen"

	agents_config = "config/agents.yaml"
	tasks_config = "config/tasks.yaml"
		

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

		
	@agent
	def coach(self) -> Agent:
		return Agent(
			config=self.agents_config['coach'],
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

	@task
	def instrucoes_coach(self) -> Task:
		return Task(
			config=self.tasks_config['instrucoes_coach'],
		)
		
	@crew
	def crew(self) -> Crew:
		return Crew(
			agents = [
				self.expert(),
				self.professor_expert(),
				self.organiza_tarefaz()
			],
			tasks=[
				self.analisar_experts(),
				self.plano_estudos(),
				self.organiza_estudos()
			],
			process=Process.sequential
		)
        
        


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
		
	
	@agent
	def coach(self) -> Agent:
		return Agent(
			config=self.agents_config['coach'],
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

	@task
	def instrucoes_coach(self) -> Task:
		return Task(
			config=self.tasks_config['instrucoes_coach'],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the EspecialistaDeliberado crew"""
		

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
	


@CrewBase
class CoachDeliberado():
	"""EspecialistaDeliberado crew"""

	agents_config = 'config/agents_coach.yaml'
	tasks_config = 'config/tasks_coach.yaml'
	
	@agent
	def progress_coach(self) -> Agent:
		return Agent(
			config=self.agents_config['progress_coach'],
			verbose=True
		)
		
	@task
	def progress_instrucoes_coach(self) -> Task:
		return Task(
			config=self.tasks_config['progress_instrucoes_coach'],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the EspecialistaDeliberado crew"""
		

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
		)
	
