# logs for kubenetes on ali with CRD

## 使用说明

- **采集模式**：目前提供两种日志采集模式：1、极简模式逐行采集常规docker log文件；2、全局正则采集docker log文件；

- **适配要求**：
    - 日志文件需要按照指定模式命名：level-servicename-*.log，如：
    `info.tsp-member-center.2018-06-12.0.log`
    `kafka.tsp-member-center.2018-06-12.log`
    - 日志内容中首行需以时间打头，格式为：yyyy-mm-dd hh:mm:ss，如：`2018-06-15 19:41:52.982` 或者`2018-06-15 19:41:52`

- **使用**:
    - 添加配置：
    极简模式逐行采集：`python add_simple-template.j2 ServiceName Level`
    全局正则多行合并：`python add_regular-template.j2 ServiceName Level`
    - 查询配置：
    `kubectl get aliyunlogconfigs`
    - 删除配置：
    `kubectl delete aliyunlogconfigs YourConfigName`
