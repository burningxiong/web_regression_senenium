#! /usr/bin/env python
#  -*- coding:utf8 -*-
# date: 2016-07-18

__author__ = 'XXX'

from selenium import webdriver
from common import *
from datas import *
import unittest


class TestAdminPortal(unittest.TestCase):
    """用于测试XXX管理门户和用户门户
    """

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(dict_portal_info['XXX_admin']['base_url'])

    def test_10_login_wrong_user_info(self):
        """测试用户名错误的情况，页面会提示“账号不存在”，测试密码错误的情况，页面会提示“密码错误”
        :return:
        """
        login(self.driver, 'iot_admin', account='asdfasd')
        assert get_tag_value(self.driver.page_source, text=u'账号不存在')
        login(self.driver, 'iot_admin', password='asdfasd')
        assert get_tag_value(self.driver.page_source, text=u'密码错误')

    def test_11_admin_change_password(self):
        """测试管理员修改密码的功能，包括输入错误原密码和输入不一致的新密码，以及重置按钮的功能
        :return:
        """
        login(self.driver, 'iot_admin')
        change_password_test(self.driver, 'iot_admin')

    def test_12_create_customer(self):
        """测试新增客户
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="username"]', customer_name),
                    ('//*[@id="password"]', customer_psw),
                    ('//*[@id="name"]', name),
                    {'xpath': '//*[@id="uniform-undefined"]/select', 'select_attr': {'name': 'industry'}},
                    {'xpath': '//*[@id="uniform-undefined"]/select', 'select_attr': {'name': 'type'}},
                    ('//*[@id="age"]', '22'),
                    {'xpath': '//*[@id="uniform-undefined"]/select', 'select_attr': {'name': 'sex'}},
                    ('//*[@id="province"]', u'重庆市'),
                    ('//*[@id="city"]', u'重庆市'),
                    ('//*[@id="addr"]', u'重庆市南岸区白鹤路98号'),
                    ('//*[@id="telno"]', get_tel_num()), '//*[@id="fo"]/p[12]/span/input[2]',
                    dict_index=dict_table['users'], value=name)

    def test_13_modify_customer(self):
        """测试修改用户的功能
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['users'], 'name')

    def test_14_query_customer(self):
        """测试查询客户功能，按客户姓名查询
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['users'])

    def test_15_create_company(self):
        """测试新增厂商
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[2]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[3]/a[2]/span',
                    ('//*[@id="name"]', name),
                    '//*[@id="fo"]/p[2]/span/input[2]', '//*[@id="fo"]/p[2]/span/input[3]',
                    ('//*[@id="address"]', u'重庆市沙坪坝区三峡广场'),
                    ('//*[@id="contact_person"]', get_name(1, 3)),
                    ('//*[@id="contact_telno"]', get_tel_num()),
                    ('//*[@id="contact_mail"]', get_email_addr()),
                    dict_index=dict_table['company_info'], value=name)

    def test_16_modify_company(self):
        """测试修改厂商，
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[2]/a', 'iMain')
        modify_test(self.driver, dict_table['company_info'], 'name')

    def test_17_query_company(self):
        """测试查询厂商
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[2]/a', 'iMain')
        query_test(self.driver, dict_table['company_info'])

    def test_18_create_model(self):
        """测试新增终端型号，新增三种不同的终端型号
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[3]/a', 'iMain')
        # 新建摄像头终端型号
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="name"]', name),
                    [dict_table['company_info'], 0, 'camera'],
                    ('//*[@id="desc"]', get_name(1, 6)),
                    {'xpath': '//*[@id="server_info.protocol"]', 'seq': '1'},
                    ('//*[@id="server_info.conn_str"]', get_url('ip')),
                    ('//*[@id="server_info.fin_func"]', get_name(1, 6)),
                    ('//*[@id="clientpid"]', get_name(0, 6)),
                    dict_index=dict_table['term_model_info'], value=name)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[3]/a', 'iMain')
        # 新建读写器终端型号
        name = get_name(1, 6)
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="name"]', name),
                    [dict_table['company_info'], 0, 'rfid'],
                    ('//*[@id="desc"]', get_name(1, 6)),
                    {'xpath': '//*[@id="server_info.protocol"]', 'seq': '2'},
                    ('//*[@id="server_info.conn_str"]', get_url('ip')),
                    ('//*[@id="server_info.fin_func"]', get_name(1, 6)),
                    ('//*[@id="clientpid"]', get_name(0, 6)),
                    dict_index=dict_table['term_model_info'], value=name)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[3]/a', 'iMain')
        # 新建rfidtag终端型号
        name = get_name(1, 6)
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="name"]', name),
                    [dict_table['company_info'], 0, 'rfidtag'],
                    ('//*[@id="desc"]', get_name(1, 6)),
                    {'xpath': '//*[@id="server_info.protocol"]', 'seq': '3'},
                    ('//*[@id="server_info.conn_str"]', get_url('ip')),
                    ('//*[@id="server_info.fin_func"]', get_name(1, 6)),
                    ('//*[@id="clientpid"]', get_name(0, 6)),
                    dict_index=dict_table['term_model_info'], value=name)

    def test_19_modify_model(self):
        """测试修改终端型号
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[3]/a', 'iMain')
        modify_test(self.driver, dict_table['term_model_info'], 'name')

    def test_20_query_model(self):
        """测试查询终端型号
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[3]/a', 'iMain')
        query_test(self.driver, dict_table['term_model_info'])

    def test_21_create_building(self):
        """测试新增建筑物
        :return:
        """
        name = get_name(1, 6)
        floors = random.randrange(1, 300)
        floor_acreage = random.randrange(100, 1000)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[4]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="desc"]', name),
                    ('//*[@id="jingdu"]', random.randrange(-180, 180)),
                    ('//*[@id="weidu"]', random.randrange(-180, 180)),
                    ('//*[@id="serial"]', random.randrange(0, 100)),
                    ('//*[@id="acreage"]', floors * floor_acreage),
                    ('//*[@id="floor_acreage"]', floor_acreage),
                    ('//*[@id="floors"]', floors),
                    ('//*[@id="high"]', str(random.uniform(4, 6))[:3]),
                    ('//*[@id="load_bearing"]', 1000),
                    ('//*[@id="structure"]', u'钢筋混泥土'),
                    dict_index=dict_table['building_info'], value=name)

    def test_22_modify_building(self):
        """测试修改建筑物
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[4]/a', 'iMain')
        modify_test(self.driver, dict_table['building_info'], 'name')

    def test_23_query_building(self):
        """测试查询建筑物
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[4]/a', 'iMain')
        query_test(self.driver, dict_table['building_info'])

    def test_24_create_room(self):
        """测试新增房间
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[5]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[3]/a[2]/span',
                    ('//*[@id="desc"]', name),
                    [dict_table['building_info'], 0],
                    ('//*[@id="floor"]', random.randrange(1, 20)),
                    ('//*[@id="X"]', random.randrange(10, 1000)),
                    ('//*[@id="Y"]', random.randrange(10, 1000)),
                    dict_index=dict_table['room_info'], value=name)

    def test_25_modify_room(self):
        """测试修改房间
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[5]/a', 'iMain')
        modify_test(self.driver, dict_table['room_info'], 'name')

    def test_26_query_room(self):
        """测试查询房间
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[5]/a', 'iMain')
        query_test(self.driver, dict_table['room_info'])

    def test_27_create_industry(self):
        """测试新增行业
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[6]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="dicname"]', name),
                    dict_index=dict_table['dictionary'], value=name)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[6]/a', 'iMain')
        # 测试不能存在相同名称的行业
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="dicname"]', name),
                    dict_index=dict_table['dictionary'], warn_num=1)

    def test_28_query_industry(self):
        """测试查询行业
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[6]/a', 'iMain')
        query_test(self.driver, dict_table['dictionary'])

    def test_29_create_trigger(self):
        """测试新增触发器
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[7]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="name"]', name),
                    [dict_table['app_info'], 0],
                    ('//*[@id="desc"]', get_name(1, 10)),
                    [dict_table['term_model_info'], 0],
                    [dict_table['reader_info'], 0],
                    {'xpath': '//*[@id="src_reqtype"]', 'select_attr': {'name': 'src_reqtype'}},
                    {'xpath': '//*[@id="regmethod"]', 'select_attr': {'name': 'regmethod'}},
                    dict_index=dict_table['triggers'], value=name)

    def test_30_modify_trigger(self):
        """测试修改触发器
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[7]/a', 'iMain')
        modify_test(self.driver, dict_table['triggers'], 'name')

    def test_31_query_trigger(self):
        """测试查询触发器
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[7]/a', 'iMain')
        query_test(self.driver, dict_table['triggers'])

    def test_32_create_gateway(self):
        """测试创建网关
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[3]/a', '//*[@id="网关管理"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="gate_name"]', name),
                    {'xpath': '//*[@id="gate_type"]', 'select_attr': {'name': 'gate_type'}},
                    ('//*[@id="gate_desc"]', get_name(1, 10)),
                    {'xpath': '//*[@id="connection_protocol"]', 'select_attr': {'name': 'connection.protocol'}},
                    {'xpath': '//*[@id="connection.host_type"]', 'select_attr': {'name': 'connection.host_type'}},
                    ('//*[@id="connection.conn_str"]', get_url()),
                    ('//*[@id="connection.url"]', get_url('http')),
                    dict_index=dict_table['gateway_info'], value=name)

    def test_33_modify_gateway(self):
        """测试修改网关
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[3]/a', '//*[@id="网关管理"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['gateway_info'], 'name')

    def test_34_query_gateway(self):
        """测试查询网关
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[3]/a', '//*[@id="网关管理"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['gateway_info'])

    def test_35_create_reader(self):
        """测试新增读写器
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[2]/a', '//*[@id="终端信息管理"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="reader_name"]', name),
                    {'xpath': '//*[@id="reader_type"]', 'select_attr': {'name': 'reader_type'}},
                    [dict_table['app_info'], 0],
                    [dict_table['company_info'], 0],
                    [dict_table['term_model_info'], 1],
                    [dict_table['gateway_info'], 0],
                    ('//*[@id="mac_addr"]', get_mac_addr()),
                    ('//*[@id="reader_desc"]', get_name(1, 10)),
                    {'xpath': '//*[@id="connection_protocol"]', 'select_attr': {'name': 'connection.protocol'}},
                    {'xpath': '//*[@id="connection.host_type"]', 'select_attr': {'name': 'connection.host_type'}},
                    ('//*[@id="conn_str"]', get_url()),
                    ('//*[@id="connection.url"]', get_url('http')),
                    {'xpath': '//*[@id="position.type"]', 'select_attr': {'name': 'position.type'}},
                    [dict_table['building_info'], 0],
                    [dict_table['room_info'], 0],
                    ('//*[@id="login_info_user"]', get_name(0, 6)),
                    ('//*[@id="login_info_password"]', get_name(2, 6)),
                    dict_index=dict_table['reader_info'], value=name)

    def test_36_modify_reader(self):
        """测试修改读写器
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[2]/a', '//*[@id="终端信息管理"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['reader_info'], 'name')

    def test_37_query_reader(self):
        """测试查询读写器
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[2]/a', '//*[@id="终端信息管理"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['reader_info'])

    def test_38_create_camera(self):
        """测试新增摄像头
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[2]/a', '//*[@id="终端信息管理"]/li[2]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[3]/a[2]/span',
                    ('//*[@id="camera_name"]', name),
                    [dict_table['company_info'], 0],
                    [dict_table['app_info'], 0],
                    [dict_table['term_model_info'], 2],
                    [dict_table['gateway_info'], 0],
                    ('//*[@id="camera_desc"]', get_name(1, 10)),
                    {'xpath': '//*[@id="connection_protocol"]', 'select_attr': {'name': 'connection.protocol'}},
                    {'xpath': '//*[@id="connection.host_type"]', 'select_attr': {'name': 'connection.host_type'}},
                    ('//*[@id="conn_str"]', get_url()),
                    ('//*[@id="connection.url"]', get_url('http')),
                    [dict_table['building_info'], 0],
                    [dict_table['room_info'], 0],
                    dict_index=dict_table['camera_info'], value=name)

    def test_39_modify_camera(self):
        """测试修改摄像头
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[2]/a', '//*[@id="终端信息管理"]/li[2]/a', 'iMain')
        modify_test(self.driver, dict_table['camera_info'], 'name')

    def test_40_query_camera(self):
        """测试查询摄像头
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[2]/a', '//*[@id="终端信息管理"]/li[2]/a', 'iMain')
        query_test(self.driver, dict_table['camera_info'])

    def test_41_create_app(self):
        """测试新增应用
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="app_name"]', name),
                    {'xpath': '//*[@id="uniform-undefined"]/select', 'select_attr': {'name': 'industry'}},
                    ('//*[@id="token"]', get_name(0, 6)),
                    ('//*[@id="sms_rate"]', random.randrange(10, 1000, 10)),
                    ('//*[@id="mms_rate"]', random.randrange(10, 1000, 10)),
                    ('//*[@id="callbackurl"]', get_url('http')),
                    ('//*[@id="app_desc"]', get_name(1, 10)),
                    dict_index=dict_table['app_info'], value=name)

    def test_42_modify_app(self):
        """测试修改应用
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['app_info'], 'name')

    def test_43_query_app(self):
        """测试查询应用
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['app_info'])

    def test_44_create_app_user(self):
        """测试新增应用与用户绑定关系
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[2]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    # 此处先填写用户名称，因为查询也是按照用户名来查询，所以关键字必须去用户名
                    [dict_table['users'], 0],
                    [dict_table['app_info'], 0],
                    dict_index=dict_table['app_user'])
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[2]/a', 'iMain')
        # 测试不能存在相同的绑定关系
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    [dict_table['users'], 0],
                    [dict_table['app_info'], 0],
                    dict_index=dict_table['app_user'], num=1)

    # -----------------------------------------test customer portal---------------------------------------
    def test_45_user_login_and_change_password(self):
        """测试用户门户登录功能，修改初始密码，及修改密码
        :return:
        """
        self.driver.get(dict_portal_info['iot_customer']['base_url'])
        login(self.driver, 'iot_customer')
        # 测试修改初始密码
        wait_xpath_input_or_click(self.driver, '//*[@id="password"]', customer_psw)
        wait_xpath_input_or_click(self.driver, '//*[@id="confirm_password"]', customer_psw)
        wait_xpath_input_or_click(self.driver, '//*[@id="fo"]/fieldset/div[4]/button[1]')
        assert self.driver.find_element_by_link_text('物联网云平台|用户门户')
        # 测试修改密码功能
        change_password_test(self.driver, 'iot_customer')

    def test_46_user_create_reader(self):
        """测试用户门户新增读写器
        :return:
        """
        reader_name = get_name(1, 6)
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[2]/a/span', 'main')
        create_test(self.driver, '/html/body/div[3]/div/div[1]/h2/button',
                    ('//*[@id="reader_name"]', reader_name),
                    {'xpath': '//*[@id="reader_type"]', 'select_attr': {'name': 'reader_type'}},
                    [dict_table['app_info'], 0],
                    [dict_table['company_info'], 0],
                    [dict_table['term_model_info'], 1],
                    [dict_table['gateway_info'], 0],
                    ('//*[@id="mac_addr"]', get_mac_addr()),
                    ('//*[@id="reader_desc"]', get_name(1, 10)),
                    {'xpath': '//*[@id="connection_protocol"]', 'select_attr': {'name': 'connection.protocol'}},
                    {'xpath': '//*[@id="connection.host_type"]', 'select_attr': {'name': 'connection.host_type'}},
                    ('//*[@id="conn_str"]', get_url()),
                    ('//*[@id="connection.url"]', get_url('http')),
                    {'xpath': '//*[@id="position.type"]', 'select_attr': {'name': 'position.type'}},
                    [dict_table['building_info'], 0],
                    [dict_table['room_info'], 0],
                    ('//*[@id="login_info_user"]', get_name(0, 6)),
                    ('//*[@id="login_info.password"]', get_name(2, 6)),
                    dict_index=dict_table['reader_info'], value=reader_name,
                    portal_type=dict_portal_info['iot_customer']['save_xpath'])

    def test_47_user_query_and_modify_reader(self):
        """测试用户门户的读写器查询和修改功能
        :return:
        """
        # 测试查询功能
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[2]/a/span', 'main')
        query_test(self.driver, dict_table['reader_info'], 'iot_customer')
        # 开始测试修改功能
        modify_test(self.driver, dict_table['reader_info'], 'name', 'iot_customer')

    def test_48_user_delete_reader(self):
        """测试用户门户的读写器的删除功能
        :return:
        """
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[2]/a/span', 'main')
        delete_test(self.driver, dict_table['reader_info'], portal_type='iot_customer')

    def test_49_user_create_camera(self):
        """测试用户门户新增摄像头的功能
        :return:
        """
        camera_name = get_name(1, 6)
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[3]/a/span', 'main')
        create_test(self.driver, '/html/body/div[3]/div/div[1]/h2/button',
                    ('//*[@id="camera_name"]', camera_name),
                    [dict_table['company_info'], 0],
                    [dict_table['app_info'], 0],
                    [dict_table['term_model_info'], 2],
                    [dict_table['gateway_info'], 0],
                    ('//*[@id="camera_desc"]', get_name(1, 10)),
                    {'xpath': '//*[@id="connection_protocol"]', 'select_attr': {'name': 'connection.protocol'}},
                    {'xpath': '//*[@id="connection.host_type"]', 'select_attr': {'name': 'connection.host_type'}},
                    ('//*[@id="conn_str"]', get_url()),
                    ('//*[@id="connection.url"]', get_url('http')),
                    [dict_table['building_info'], 0],
                    [dict_table['room_info'], 0],
                    dict_index=dict_table['camera_info'], value=camera_name,
                    portal_type=dict_portal_info['iot_customer']['save_xpath'])

    def test_50_user_query_and_modify_camera(self):
        """测试用户门户的摄像头查询和修改功能
        :return:
        """
        # 测试查询功能
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[3]/a/span', 'main')
        query_test(self.driver, dict_table['camera_info'], 'iot_customer')
        # 开始测试修改功能
        modify_test(self.driver, dict_table['camera_info'], 'name', 'iot_customer')

    def test_51_user_delete_camera(self):
        """测试用户门户摄像头删除功能
        :return:
        """
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[3]/a/span', 'main')
        delete_test(self.driver, dict_table['app_info'], portal_type='iot_customer')

    def test_52_user_create_rfid_tag(self):
        """测试用户门户新增rfid标签
        :return:
        """
        epc = get_name(1, 6)
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[5]/a', 'main')
        create_test(self.driver, '/html/body/div[3]/div/div[1]/h2/button',
                    ('//*[@id="tid"]', get_name(0, 8)),
                    ('//*[@id="epc"]', epc),
                    ('//*[@id="userdata"]', get_name(0, 8)),
                    [dict_table['company_info'], 0],
                    [dict_table['term_model_info'], 0],
                    [dict_table['app_info'], 0],
                    dict_index=dict_table['rfid_tags'], value=epc,
                    portal_type=dict_portal_info['iot_customer']['save_xpath'])

    def test_53_user_query_modify_rfid_tag(self):
        """测试rfid标签的查询和修改功能
        :return:
        """
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[5]/a', 'main')
        query_test(self.driver, dict_table['rfid_tags'], 'iot_customer')
        # 开始测试修改标签
        modify_test(self.driver, dict_table['rfid_tags'], 'name', 'iot_customer')

    def test_54_user_delete_rfid_tag(self):
        """测试删除rfid标签功能
        :return:
        """
        get_page(self.driver, '/html/body/div[2]/div[1]/div[1]/div/ul/li[5]/a', 'main')
        delete_test(self.driver, dict_table['rfid_tags'], portal_type='iot_customer')

    # -----------------------------------------end of testing customer portal-------------------------------
    def test_55_modify_app_user(self):
        """测试修改应用与用户绑定关系
        :return:
        """
        self.driver.get(dict_portal_info['iot_admin']['base_url'])
        login(self.driver, 'iot_admin')
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[2]/a', 'iMain')
        modify_test(self.driver, dict_table['app_user'])

    def test_56_query_app_user(self):
        """测试查询应用应用与用户绑定关系
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[2]/a', 'iMain')
        query_test(self.driver, dict_table['app_user'])

    def test_57_create_rfid_tags(self):
        """测试新增标签
        :return:
        """
        epc = get_name(0, 8)
        get_page(self.driver, '//*[@id="leftmenu"]/li[5]/a', '//*[@id="标识信息管理"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="tid"]', get_name(0, 8)),
                    ('//*[@id="epc"]', epc),
                    ('//*[@id="userdata"]', get_name(0, 8)),
                    [dict_table['users'], 0],
                    [dict_table['company_info'], 0],
                    [dict_table['term_model_info'], 0],
                    [dict_table['app_info'], 0],
                    dict_index=dict_table['rfid_tags'], value=epc)

    def test_58_modify_rfid_tags(self):
        """测试修改标签
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[5]/a', '//*[@id="标识信息管理"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['rfid_tags'], 'name')

    def test_59_query_rfid_tags(self):
        """测试查询标签
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[5]/a', '//*[@id="标识信息管理"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['rfid_tags'])

    def test_60_create_term_param(self):
        """测试新增终端型号参数
        :return:
        """
        procname = get_name(0, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[6]/a', '//*[@id="终端参数管理"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    [dict_table['term_model_info'], 0],
                    {'xpath': '//*[@id="msgtype"]', 'select_attr': {'name': 'msgtype'}},
                    ('//*[@id="procname"]', procname),
                    ('//*[@id="libinfo.libname"]', get_name(0, 6)),
                    ('//*[@id="libinfo.func"]', get_name(0, 6)),
                    dict_index=dict_table['term_ability_map'], value=procname)

    def test_61_modify_term_param(self):
        """测试修改终端型号参数
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[6]/a', '//*[@id="终端参数管理"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['term_ability_map'], 'name')

    def test_62_query_term_param(self):
        """测试查询终端型号参数
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[6]/a', '//*[@id="终端参数管理"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['term_ability_map'])

    def test_63_create_term_template(self):
        """测试新增终端型号参数模板
        :return:
        """
        template_name = get_name(0, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[6]/a', '//*[@id="终端参数管理"]/li[2]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    [dict_table['term_model_info'], 0],
                    ('//*[@id="template_name"]', template_name),
                    ('//*[@id="parameters"]', get_name(0, 6)), '//*[@id="fo"]/p[3]/span/a/span',
                    ('//*[@id="fo"]/p[4]/span/input', get_name(0, 6)), '//*[@id="fo"]/p[3]/span/a/span',
                    ('//*[@id="fo"]/p[5]/span/input', get_name(0, 6)), '//*[@id="fo"]/p[3]/span/a/span',
                    '//*[@id="fo"]/p[6]/span/a/span',
                    dict_index=dict_table['term_param_template'], value=template_name)

    def test_64_modify_term_template(self):
        """测试修改终端型号参数模板
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[6]/a', '//*[@id="终端参数管理"]/li[2]/a', 'iMain')
        modify_test(self.driver, dict_table['term_param_template'], 'name')

    def test_65_query_term_template(self):
        """测试查询终端型号参数模板
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[6]/a', '//*[@id="终端参数管理"]/li[2]/a', 'iMain')
        query_test(self.driver, dict_table['term_param_template'])

    def test_66_create_app_term(self):
        """测试新增订购关系
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[7]/a', '//*[@id="订购关系管理"]/li[1]/a', 'iMain')
        # 测试同一个应用之间进行授权，页面会有错误提示
        create_test(self.driver, '//*[@id="fo"]/p[3]/a[2]/span',
                    # ['//*[@id="fo"]/p[1]/span/a/span', dict_title['gc_iot'], '360', '520'],
                    [dict_table['app_info'], 0],
                    [dict_table['app_info_1'], 0],
                    dict_index=dict_table['authorize_info'], warn_num=1)
        get_page(self.driver, '//*[@id="leftmenu"]/li[7]/a', '//*[@id="订购关系管理"]/li[1]/a', 'iMain')
        # 测试应用a给应用b授权
        create_test(self.driver, '//*[@id="fo"]/p[3]/a[2]/span',
                    [dict_table['app_info'], 0],
                    [dict_table['app_info_1'], 1],
                    dict_index=dict_table['authorize_info'])
        # 测试不能存在两条相同的授权
        get_page(self.driver, '//*[@id="leftmenu"]/li[7]/a', '//*[@id="订购关系管理"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[3]/a[2]/span',
                    [dict_table['app_info'], 0],
                    [dict_table['app_info_1'], 1],
                    dict_index=dict_table['authorize_info'], num=1)

    def test_67_modify_app_term(self):
        """测试修改订购关系
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[7]/a', '//*[@id="订购关系管理"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['authorize_info'])

    def test_68_query_app_term(self):
        """测试查询订购关系
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[7]/a', '//*[@id="订购关系管理"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['authorize_info'])

    def test_69_create_schedule(self):
        """测试新增定时任务
        :return:
        """
        # 为了关闭日历控件，需要多点一下最后一个输入框
        get_page(self.driver, '//*[@id="leftmenu"]/li[8]/a', '//*[@id="终端数据管理"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[4]/a[2]/span',
                    [dict_table['term_model_info'], 1],
                    [dict_table['reader_info'], 0],
                    {'xpath': '//*[@id="reqtype"]', 'select_attr': {'name': 'reqtype'}},
                    [dict_table['app_info'], 0],
                    ('//*[@id="starttime"]', get_datetime(2017, 7, 15)), '//*[@id="interval"]',
                    ('//*[@id="interval"]', str(random.randrange(5, 1000, 5))),
                    dict_index=dict_table['op_schedule'])

    def test_70_modify_schedule(self):
        """测试修改定时任务
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[8]/a', '//*[@id="终端数据管理"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['op_schedule'], '')

    def test_71_create_external_system(self):
        """测试新增外部系统
        :return:
        """
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[10]/a', '//*[@id="外部系统"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="name"]', name),
                    ('//*[@id="url"]', 'http://www.baidu.com'),
                    dict_index=dict_table['external_system'], value=name)
        # 点击进入，检查是否打开了百度窗口
        get_page(self.driver, '//*[@id="leftmenu"]/li[10]/a', '//*[@id="外部系统"]/li[1]/a', 'iMain', '')
        wait_xpath_input_or_click(self.driver, '//*[@id="contentwrapper"]/table/tbody/tr[1]/td[2]/a/span')
        baidu_handle = self.driver.window_handles[1]
        self.driver.switch_to.window(baidu_handle)
        assert self.driver.title == u'百度一下，你就知道'
        self.driver.get(dict_portal_info['iot_admin']['base_url'])
        login(self.driver, 'iot_admin')

    def test_72_modify_external_system(self):
        """测试修改外部系统
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[10]/a', '//*[@id="外部系统"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['external_system'], 'name')

    def test_73_query_external_system(self):
        """测试查询外部系统
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[10]/a', '//*[@id="外部系统"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['external_system'])

    def test_74_create_role(self):
        """测试新增角色
        :return:
        """
        role_name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="rolename"]', role_name),
                    ('//*[@id="roledesc"]', get_name(1, 10)),
                    '//*[@id="fo"]/p[3]/span/div[1]/span/input',
                    '//*[@id="fo"]/p[3]/span/div[2]/span/input',
                    '//*[@id="fo"]/p[4]/span/div[1]/span/input',
                    '//*[@id="fo"]/p[5]/span/div[1]/span/input',
                    '//*[@id="fo"]/p[6]/span/div[1]/span/input',
                    dict_index=dict_table['t_role'], value=role_name)

    def test_75_modify_role(self):
        """测试修改角色
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[1]/a', 'iMain')
        modify_test(self.driver, dict_table['t_role'], 'name')

    def test_76_query_role(self):
        """测试查询角色
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[1]/a', 'iMain')
        query_test(self.driver, dict_table['t_role'])

    def test_77_create_operator(self):
        """测试新增管理员
        :return:
        """
        name = get_name(1, 6)
        account = get_name(0, 6)
        password = get_name(0, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[2]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="account"]', account),
                    ('//*[@id="name"]', name),
                    ('//*[@id="password"]', password),
                    ('//*[@id="mobile"]', get_tel_num()),
                    ('//*[@id="email"]', get_email_addr()),
                    [dict_table['t_role'], 0],
                    dict_index=dict_table['t_operator'], value=name)
        # 退出门户，检查新建的账户能否成功登录
        self.driver.refresh()
        logout(self.driver, 'iot_admin')
        login(self.driver, 'iot_admin', account=account, password=password)
        assert self.driver.find_element_by_xpath(dict_portal_info['iot_admin']['logout'][0]).text == name
        # 新增的管理员具备新增客户的权限，测试子管理员新增客户
        name = get_name(1, 6)
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[1]/a', 'iMain')
        create_test(self.driver, '//*[@id="fo"]/p[2]/a[2]/span',
                    ('//*[@id="username"]', get_name(0, 6)),
                    ('//*[@id="password"]', get_name(2, 6)),
                    ('//*[@id="name"]', name),
                    {'xpath': '//*[@id="uniform-undefined"]/select', 'select_attr': {'name': 'industry'}},
                    {'xpath': '//*[@id="uniform-undefined"]/select', 'select_attr': {'name': 'type'}},
                    ('//*[@id="age"]', '22'),
                    {'xpath': '//*[@id="uniform-undefined"]/select', 'select_attr': {'name': 'sex'}},
                    ('//*[@id="province"]', u'重庆市'),
                    ('//*[@id="city"]', u'重庆市'),
                    ('//*[@id="addr"]', u'重庆市南岸区白鹤路98号'),
                    ('//*[@id="telno"]', get_tel_num()), '//*[@id="fo"]/p[12]/span/input[2]',
                    dict_index=dict_table['users'], value=name)
        # 删除新增的管理员
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['users'])
        self.driver.get(dict_portal_info['iot_admin']['base_url'])
        login(self.driver, 'iot_admin')

    def test_78_modify_operator(self):
        """ 测试修改管理员
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[2]/a', 'iMain')
        modify_test(self.driver, dict_table['t_operator'], 'name')

    def test_79_query_operator(self):
        """测试查询管理员
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[2]/a', 'iMain')
        query_test(self.driver, dict_table['t_operator'])

    # -----------------------------------------delete test data---------------------------------------
    def test_80_delete_app_user(self):
        """测试删除应用与用户绑定关系
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[2]/a', 'iMain')
        delete_test(self.driver, dict_table['app_user'])

    def test_81_delete_industry(self):
        """测试删除行业
        :return:
        """
        login(self.driver, 'iot_admin', account='admin', password='admin@1501')
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[6]/a', 'iMain')
        delete_test(self.driver, dict_table['dictionary'])

    def test_82_delete_trigger(self):
        """测试删除触发器
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[7]/a', 'iMain')
        delete_test(self.driver, dict_table['triggers'])

    def test_83_delete_rfid_tag(self):
        """测试删除rfid标签
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[5]/a', '//*[@id="标识信息管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['rfid_tags'])

    def test_84_delete_term_params(self):
        """测试删除终端型号参数
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[6]/a', '//*[@id="终端参数管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['term_ability_map'])

    def test_85_delete_term_template(self):
        """测试删除终端型号参数模板
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[6]/a', '//*[@id="终端参数管理"]/li[2]/a', 'iMain')
        delete_test(self.driver, dict_table['term_param_template'])

    def test_86_delete_app_term(self):
        """测试删除订购关系
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[7]/a', '//*[@id="订购关系管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['authorize_info'])

    def test_87_delete_schedule(self):
        """测试删除定时任务
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[8]/a', '//*[@id="终端数据管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['op_schedule'])

    def test_88_delete_external_system(self):
        """测试删外部系统
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[10]/a', '//*[@id="外部系统"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['external_system'])

    def test_89_delete_reader(self):
        """测试删除读写器
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[2]/a', '//*[@id="终端信息管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['reader_info'])

    def test_90_delete_camera(self):
        """测试删除摄像头
        :return:
        """

        get_page(self.driver, '//*[@id="leftmenu"]/li[2]/a', '//*[@id="终端信息管理"]/li[2]/a', 'iMain')
        delete_test(self.driver, dict_table['camera_info'])

    def test_91_delete_room(self):
        """测试删除房间
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[5]/a', 'iMain')
        delete_test(self.driver, dict_table['room_info'])

    def test_92_delete_gateway(self):
        """测试删除网关
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[3]/a', '//*[@id="网关管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['gateway_info'])

    def test_93_delete_building(self):
        """测试删除建筑物
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[4]/a', 'iMain')
        delete_test(self.driver, dict_table['building_info'])

    def test_94_delete_company(self):
        """测试删除厂商
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[2]/a', 'iMain')
        delete_test(self.driver, dict_table['company_info'])

    def test_95_delete_model(self):
        """测试终端型号删除
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[3]/a', 'iMain')
        delete_test(self.driver, dict_table['term_model_info'])

    def test_96_delete_app(self):
        """测试删除应用
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[4]/a', '//*[@id="应用信息管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['app_info'])

    def test_97_delete_customer(self):
        """测试删除客户功能
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[1]/a', '//*[@id="基础数据维护"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['users'])

    def test_98_delete_role(self):
        """测试删除角色
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['t_role'], 1)

    def test_99_delete_operator(self):
        """测试删除管理员
        :return:
        """
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[2]/a', 'iMain')
        delete_test(self.driver, dict_table['t_operator'])
        # 删除管理员之后才能删除掉对应的角色
        get_page(self.driver, '//*[@id="leftmenu"]/li[11]/a', '//*[@id="系统管理"]/li[1]/a', 'iMain')
        delete_test(self.driver, dict_table['t_role'])

    def test_end(self):
        """测试结束
        :return:
        """
        self.driver.quit()

if __name__ == '__main__':
    # unittest.main()
    create_test_report(TestAdminPortal, 'XXX管理门户自动化测试报告', 'XXX管理门户自动化测试报告')