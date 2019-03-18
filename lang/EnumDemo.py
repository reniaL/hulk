# coding=utf-8


from enum import Enum


class VideoStatus(Enum):
    DELETED = -1
    TODO = 20
    DONE = 50


class EnumDemo(object):

    def simple(self):
        """简单的声明枚举类
        """
        log_types = Enum('LogType', ('select', 'insert', 'delete', 'update'))

        for log_type in log_types:
            print log_type, log_type.value

        print log_types.insert.value
        print log_types['select']
        print log_types(4)


if __name__ == '__main__':
    demo = EnumDemo()
    demo.simple()

    status = VideoStatus.DONE
    print status.value
    print status == VideoStatus.DONE  # true
    print VideoStatus(-1)  # VideoStatus.DELETED
