# logs for kubenetes on ali with CRD

## 使用说明
> 用来通过CRD管理日志采集配置，在安装完logtail之后，需要进行相关配置以输出日志到阿里log，有两种配置方式，一种是在日志控制台配置，另一种就是CRD的配置方式，可以直接使用kubectl对配置进行管理，这里提供CRD的管理脚本（python），说明如下：
- **原理**：
    - 脚本参数传入服务名和日志等级，结合模版生成yaml编排文件，进而创建相应的资源对象

- **采集模式**：目前提供两种日志采集模式：
    - 1、简单文本模式逐行采集常规docker log文件，对应脚本：add_simple_log.py；
    - 2、全局正则采集（整合堆栈信息）docker log文件，对应脚本：add_regular_log.py；

- **适配要求**：
    - 日志文件需要按照指定模式命名：level-servicename-*.log，如：
    `info.tsp-member-center.2018-06-12.0.log`
    `kafka.tsp-member-center.2018-06-12.log`
    - 日志内容中首行需以时间打头，格式为：yyyy-mm-dd hh:mm:ss，如：`2018-06-15 19:41:52.982` 或者`2018-06-15 19:41:52`

- **使用**:
    - 添加配置：
    极简模式逐行采集：`python add_simple_log.py ServiceName Level`
    全局正则多行合并：`python add_regular_log.py ServiceName Level`
    - 查询配置：
    `kubectl get aliyunlogconfigs`
    - 删除配置：
    `kubectl delete aliyunlogconfigs YourConfigName`
