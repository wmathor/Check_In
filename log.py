import os, logging
logFilename = os.getcwd() + '\\执行日志.log'
print(logFilename)

def logging_out(logContext):
    ''''' Output log to file and console '''
    # Define a Handler and set a format which output to file
    logging.basicConfig(
        level = logging.INFO,  # 定义输出到文件的log级别，大于此级别的都被输出
        format = '%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式        
        datefmt = '%Y-%m-%d %A %H:%M:%S',  # 时间
        filename = logFilename,  # log文件名
        filemode = 'a')  # 写入模式“w”或“a”
    logging.info(logContext)

if __name__ == '__main':
    logging_out('签到成功')