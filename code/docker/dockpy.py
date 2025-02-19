''' docker api example'''
import docker
IMAGE_LIST = ["bfirsh/reticulate-splines",
              "alpine",
              "busybox",
              "httpd"]


def main():
    ''' main function'''
    client = docker.from_env()
    for image in IMAGE_LIST:
        client.images.pull(image)
        if image == "httpd":
            client.containers.run(image, ports={'80/tcp': 8080}, detach=True)
        else:
            client.containers.run(image, detach=True)
    for line in client.containers.list():
        print(f"{line.id} : {line.name}")
    for item in client.containers.list():
        item.stop()
    for vm in client.containers.list():
        vm.remove()
    client.close()


if __name__ == '__main__':
    main()
