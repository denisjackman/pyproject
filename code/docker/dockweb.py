''' docker api example'''
import docker


def main():
    ''' main function'''
    client = docker.from_env()
    client.containers.run("httpd", ports={'80/tcp': 8080}, detach=True)
    client.close()


if __name__ == '__main__':
    main()
