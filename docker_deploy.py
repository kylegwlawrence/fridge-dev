from prefect.deployments import Deployment
from main import main

from prefect.infrastructure.docker import DockerContainer

docker_block = DockerContainer.load("fridge-dev")

docker_deployment = Deployment.build_from_flow(
    flow=main
    , name='docker-flow'
    , infrastructure=docker_block
)

if __name__=='__main__':
    docker_deployment.apply()
