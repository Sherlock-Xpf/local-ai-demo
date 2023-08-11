# For prerequisites running the following sample, visit https://help.aliyun.com/document_detail/611472.html
from http import HTTPStatus

from dashscope import Generation

def simple_sample():
    # 模型可以为模型列表中任一模型
    response = Generation.call(model='llama2-7b-chat-v2',
                               prompt='Hey, are you conscious? Can you talk to me?')
    if response.status_code == HTTPStatus.OK:
        print('Result is: %s' % response.output)
    else:
        print('Failed request_id: %s, status_code: %s, code: %s, message:%s' %
              (response.request_id, response.status_code, response.code,
               response.message))


if __name__ == '__main__':
    simple_sample()

