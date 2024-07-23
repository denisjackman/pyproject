''' docker api example'''
import docker


def dkr_create(dkrc_image, dkrc_port, dkrc_name):
    ''' start a docker container '''
    dkrc_client = docker.from_env()
    dkrc_client.containers.run(dkrc_image,
                               ports={'80/tcp': dkrc_port},
                               detach=True,
                               name=dkrc_name)
    dkrc_client.close()


def dkr_stop(dkrs_name):
    ''' stop a docker container '''
    dkrs_client = docker.from_env()
    dkrs_container = dkrs_client.containers.get(dkrs_name)
    dkrs_container.stop()
    dkrs_client.close()


def dkr_start(dkrs_name):
    ''' start a docker container '''
    dkrs_client = docker.from_env()
    dkrs_container = dkrs_client.containers.get(dkrs_name)
    dkrs_container.start()
    dkrs_client.close()


def dkr_remove(dkrr_name):
    ''' remove a docker container '''
    dkrr_client = docker.from_env()
    dkrr_container = dkrr_client.containers.get(dkrr_name)
    dkr_stop(dkrr_name)
    dkrr_container.remove()
    dkrr_client.close()


def main():
    ''' main function'''
    dkr_create("httpd", 8083, "web3")
    dkr_start("jackmanimation-web")
    dkr_stop("web1")
    dkr_remove("web2")


if __name__ == '__main__':
    main()
