import datetime
import GlobalVariable as GV
import copy

def GetTodayDateTime():
    Today=datetime.datetime.now()
    print(Today)
    DateTime = datetime.datetime.strftime(Today, '%Y-%m-%d')
    print(DateTime)

def ExtractPublicTaskInfo(MysqlObject):
    try:
        GV.ExtractPublicTaskInfoDict={'ExtractTaskID':{}}
        ExtractTaskInfo = {'labelname': '', 'filename': '', 'status': '', 'createtime': '', 'endtime': ''}

        MysqlCommand = "select labelname,filename,status,DATE_FORMAT(createtime,'%%Y-%%m-%%d %%H:%%i:%%S'),DATE_FORMAT(endtime,'%%Y-%%m-%%d %%H:%%i:%%S') from %s.label_group_personas where createtime>'2018-05-13' and status=4;" % MysqlObject._UseDatabase
        MysqlObject._MysqlCursor.execute(MysqlCommand)
        PublicBatchInfoTupleList = MysqlObject._MysqlCursor.fetchall()

        for PublicBatchInfoTupleIndex in range(len(PublicBatchInfoTupleList)):
            if PublicBatchInfoTupleIndex+1 not in GV.ExtractPublicTaskInfoDict['ExtractTaskID']:
                GV.ExtractPublicTaskInfoDict['ExtractTaskID'][PublicBatchInfoTupleIndex+1]=copy.deepcopy(GV.ExtractTaskInfo)
                GV.ExtractPublicTaskInfoDict['ExtractTaskID'][PublicBatchInfoTupleIndex + 1]['labelname']=PublicBatchInfoTupleList[PublicBatchInfoTupleIndex][0]
                GV.ExtractPublicTaskInfoDict['ExtractTaskID'][PublicBatchInfoTupleIndex + 1]['filename']=PublicBatchInfoTupleList[PublicBatchInfoTupleIndex][1]
                GV.ExtractPublicTaskInfoDict['ExtractTaskID'][PublicBatchInfoTupleIndex + 1]['status']=PublicBatchInfoTupleList[PublicBatchInfoTupleIndex][2]
                GV.ExtractPublicTaskInfoDict['ExtractTaskID'][PublicBatchInfoTupleIndex + 1]['createtime']=PublicBatchInfoTupleList[PublicBatchInfoTupleIndex][3]
                GV.ExtractPublicTaskInfoDict['ExtractTaskID'][PublicBatchInfoTupleIndex + 1]['endtime']=PublicBatchInfoTupleList[PublicBatchInfoTupleIndex][4]

    except Exception as result:
        print("提取任务批次信息失败！ %s" % result)

