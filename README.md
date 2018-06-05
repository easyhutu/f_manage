# service-task-queue
## 任务队列调度服务
简述： 通过api对算法模块任务执行进行调度，管理
### 1.项目目录结构
> doc
* 存放项目文档，如开发文档
> task_app
* 本项目APP，包括接口管理，模型管理，辅助工具等
> test
* 项目单元测试case目录
### 2. 项目说明
##### 开发环境： Python3.6.1
#### 启动
1.安装依赖
```
pip install -r requirements.txt
```
2.启动APP
```
python main.py
```
#### 运行单元测试
```
nosetests ./test
```
### 3、配置注意事项
#### 环境变量配置
* SASL_PLAIN_PASSWORD 参数是阿里云的AccessKeySecret后10位；
* SASL_PLAIN_USERNAME 参数是阿里云的AccessKeyId
* DEFAULT_ENV 参数是配置当前项目的环境，可配置为UNITTEST/TEST/STAGE/PRODUCTION在正式环境中，请设置为PRODUCTION
#### 算法模块规则config.yaml 配置
* service 支持的算法模块名称，增加一个算法模块名称需要在source_db中增加对应数据源配置
* source_db 数据源相关配置， 其中的key 需要与service中的算法模块名称对应
* topic_name 该算法模块对应的消息队列topic的名称
* consumer_id 对应的消费者id的名称
> 消息队列默认使用partition是0，提供的消息队列消费者demo在/task_app/helpers/consumer_demo.py，
同级目录放置的ca-cert文件是阿里云证书文件
