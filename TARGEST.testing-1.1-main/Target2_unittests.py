import unittest
import Targest2

class TestGenerateReport(unittest.TestCase):
    Targest2.generateReport()

    def test_filename(self):
        expected_output = ["HDS_new_pump", "HRS_new_pump","HTP_new_pump", "HTR_new_pump", "PRS_new_pump", "RiskAnalysis_Pump",
                           "SDS_New_pump_x04", "SRS_ACE_Pump_X01", "SRS_BolusCalc_Pump_X04", "SRS_DosingAlgorithm_X03",
                           "SVaP_new_pump", "SVaTR_new_pump", "SVeTR_new_pump", "URS_new_pump"]

        self.assertEqual(Targest2.filename_collection, expected_output)

    def test_parent_tags(self):
        expected_output = [['PUMP:HRD:100', 'PUMP:HRD:105', 'PUMP:HRD:1000', 'PUMP:HRD:3330', 'PUMP:HRD:3350'],
                           ['PUMP:HRS:100', 'PUMP:HRS:105', 'PUMP:HRS:1000', 'PUMP:HRS:3330', 'PUMP:HRS:3340',
                            'PUMP:HRS:3350'], ['PUMP:HTP:100', 'PUMP:HTP:200', 'PUMP:HTP:300', 'PUMP:HTP:400',
                            'PUMP:HTP:500', 'PUMP:HTP:1100', 'PUMP:HTP:1200', 'PUMP:HTP:1300', 'PUMP:HTP:1400',
                            'PUMP:HTP:1500'], ['PUMP:HTR:100', 'PUMPHTR:200', 'PUMP:HTR:300', 'PUMP:HTR:400',
                            'PUMP:HTR:500', 'PUMP:HTR:1100', 'PUMP:HTR:1200', 'PUMP:HTR:1300', 'PUMP:HTR:1400',
                            'PUMP:HTR:1500'],['PUMP:PRS:1', 'PUMP:PRS:2', 'PUMP:PRS:3', 'PUMP:PRS:4', 'PUMP:PRS:5',
                            'PUMP:PRS:8', 'PUMP:PRS:10', 'PUMP:PRS:100', 'PUMP:PRS:105', 'PUMP:PRS:1000',
                            'PUMP:PRS:3330', 'PUMP:PRS:3340', 'PUMP:PRS:3350', 'PUMP:PRS:4000'],['PUMP:RISK:10',
                            'PUMP:RISK:20', 'PUMP:RISK:30', 'PUMP:RISK:40', 'PUMP:RISK:50'], ['PUMP:SDS:10',
                            'PUMP:SDS:20', 'PUMP:SDS:30', 'PUMP:SDS:40', 'PUMP:SDS:50', 'PUMP:SDS:60', 'PUMP:SDS:70'],
                           ['ACE:SRS:1', 'ACE:SRS:2', 'ACE:SRS:5', 'ACE:SRS:6', 'ACE:SRS:10', 'ACE:SRS:100'],
                           ['BOLUS:SRS:1', 'BOLUS:SRS:2', 'BOLUS:SRS:5', 'BOLUS:SRS:6', 'BOLUS:SRS:8', 'BOLUS:SRS:12'],
                           ['AID:SRS:1', 'AID:SRS:2', 'AID:SRS:10', 'AID:SRS:12', 'AID:SRS:20'], ['PUMP:SVAL:100',
                            'PUMP:SVAL:200', 'PUMP:SVAL:300', 'PUMP:SVAL:400', 'PUMP:SVAL:500'], ['PUMP:SVATR:100',
                            'PUMP:SVATR:200', 'PUMP:SVATR:300', 'PUMP:SVATR:400', 'PUMP:SVATR:500'], ['PUMP:UT:100',
                            'PUMP:UT:110', 'PUMP:UT:120', 'PUMP:UT:130', 'PUMP:UT:140', 'PUMP:UT:150', 'PUMP:UT:160',
                            'PUMP:UT:170', 'PUMP:UT:180', 'PUMP:UT:190', 'PUMP:UT:200', 'PUMP:UT:210', 'PUMP:UT:220',
                            'PUMP:INS:100', 'PUMP:INS:110', 'PUMP:INS:120', 'PUMP:INS:130', 'PUMP:INS:140',
                            'PUMP:INS:150', 'PUMP:INS:160', 'PUMP:INS:170', 'PUMP:INS:180', 'PUMP:INS:190',
                            'PUMP:INS:200', 'PUMP:INS:210', 'PUMP:INS:220'], ['PUMP:URS:1', 'PUMP:URS:3', 'PUMP:URS:8',
                            'PUMP:URS:10', 'PUMP:URS:100', 'PUMP:URS:103', 'PUMP:URS:1000', 'PUMP:URS:3330',
                            'PUMP:URS:3350', 'PUMP:URS:4000']]

        self.assertEqual(Targest2.parents_list, expected_output)

    def test_orphan_child_tags(self):
        expected_output = ['PUMP:URS:1', 'PUMP:URS:3', 'PUMP:URS:8', 'PUMP:URS:10', 'PUMP:URS:100', 'PUMP:URS:103',
                            'PUMP:URS:1000', 'PUMP:URS:3330', 'PUMP:URS:3350', 'PUMP:URS:4000']

        self.assertEqual(Targest2.orphanChild, expected_output)

    def test_child_tags(self):
        expected_output = [['PUMP:HRD:100', 'PUMP:HRD:105', 'PUMP:HRD:1000', 'PUMP:HRD:3330', 'PUMP:HRD:3350'],
                           ['PUMP:HRS:100', 'PUMP:HRS:105', 'PUMP:HRS:1000', 'PUMP:HRS:3330', 'PUMP:HRS:3340',
                            'PUMP:HRS:3350'], ['PUMP:HTP:100', 'PUMP:HTP:200', 'PUMP:HTP:300', 'PUMP:HTP:400',
                            'PUMP:HTP:500', 'PUMP:HTP:1100', 'PUMP:HTP:1200', 'PUMP:HTP:1300', 'PUMP:HTP:1400',
                            'PUMP:HTP:1500'], ['PUMP:HTR:100', 'PUMPHTR:200', 'PUMP:HTR:300', 'PUMP:HTR:400',
                            'PUMP:HTR:500', 'PUMP:HTR:1100', 'PUMP:HTR:1200', 'PUMP:HTR:1300', 'PUMP:HTR:1400',
                            'PUMP:HTR:1500'], ['PUMP:PRS:1', 'PUMP:PRS:2', 'PUMP:PRS:3', 'PUMP:PRS:4', 'PUMP:PRS:5',
                            'PUMP:PRS:8', 'PUMP:PRS:10', 'PUMP:PRS:100', 'PUMP:PRS:105', 'PUMP:PRS:1000',
                            'PUMP:PRS:3330', 'PUMP:PRS:3340', 'PUMP:PRS:3350', 'PUMP:PRS:4000'], ['PUMP:RISK:10',
                            'PUMP:RISK:20', 'PUMP:RISK:30', 'PUMP:RISK:40', 'PUMP:RISK:50'], ['PUMP:SDS:10',
                            'PUMP:SDS:20', 'PUMP:SDS:30', 'PUMP:SDS:40', 'PUMP:SDS:50', 'PUMP:SDS:60', 'PUMP:SDS:70'],
                           ['ACE:SRS:1', 'ACE:SRS:2', 'ACE:SRS:5', 'ACE:SRS:6', 'ACE:SRS:10', 'ACE:SRS:100'],
                           ['BOLUS:SRS:1', 'BOLUS:SRS:2', 'BOLUS:SRS:5', 'BOLUS:SRS:6', 'BOLUS:SRS:8', 'BOLUS:SRS:12'],
                           ['AID:SRS:1', 'AID:SRS:2', 'AID:SRS:10', 'AID:SRS:12', 'AID:SRS:20'], ['PUMP:SVAL:100',
                            'PUMP:SVAL:200', 'PUMP:SVAL:300', 'PUMP:SVAL:400', 'PUMP:SVAL:500'], ['PUMP:SVATR:100',
                            'PUMP:SVATR:200', 'PUMP:SVATR:300', 'PUMP:SVATR:400', 'PUMP:SVATR:500'], ['PUMP:UT:100',
                            'PUMP:UT:110', 'PUMP:UT:120', 'PUMP:UT:130', 'PUMP:UT:140', 'PUMP:UT:150', 'PUMP:UT:160',
                            'PUMP:UT:170', 'PUMP:UT:180', 'PUMP:UT:190', 'PUMP:UT:200', 'PUMP:UT:210', 'PUMP:UT:220',
                            'PUMP:INS:100', 'PUMP:INS:110', 'PUMP:INS:120', 'PUMP:INS:130', 'PUMP:INS:140',
                            'PUMP:INS:150', 'PUMP:INS:160', 'PUMP:INS:170', 'PUMP:INS:180', 'PUMP:INS:190',
                            'PUMP:INS:200', 'PUMP:INS:210', 'PUMP:INS:220'], ['PUMP:URS:1', 'PUMP:URS:3', 'PUMP:URS:8',
                            'PUMP:URS:10', 'PUMP:URS:100', 'PUMP:URS:103', 'PUMP:URS:1000', 'PUMP:URS:3330',
                            'PUMP:URS:3350', 'PUMP:URS:4000']]
        self.assertEqual(Targest2.child_tags_list, expected_output)

    Targest2.generateReport2()
    def test_childless_tags(self):
        expected_output = ['PUMP:HRS:3340', 'PUMP:HTR:100', 'PUMP:HTR:1100', 'PUMP:HTR:1200', 'PUMP:HTR:1300',
                            'PUMP:HTR:1400', 'PUMP:HTR:1500', 'PUMP:HTR:300', 'PUMP:HTR:400', 'PUMP:HTR:500',
                            'PUMP:INS:100', 'PUMP:INS:110', 'PUMP:INS:120', 'PUMP:INS:130', 'PUMP:INS:140',
                            'PUMP:INS:150', 'PUMP:INS:160', 'PUMP:INS:170', 'PUMP:INS:180', 'PUMP:INS:190',
                            'PUMP:INS:200', 'PUMP:INS:210', 'PUMP:INS:220', 'PUMP:PRS:2', 'PUMP:PRS:3340',
                            'PUMP:SDS:10', 'PUMP:SDS:20', 'PUMP:SDS:30', 'PUMP:SDS:40', 'PUMP:SDS:50', 'PUMP:SDS:60',
                            'PUMP:SDS:70', 'PUMP:SVATR:100', 'PUMP:SVATR:200', 'PUMP:SVATR:300', 'PUMP:SVATR:400',
                            'PUMP:SVATR:500', 'PUMP:UT:100', 'PUMP:UT:110', 'PUMP:UT:120', 'PUMP:UT:130',
                            'PUMP:UT:140', 'PUMP:UT:150', 'PUMP:UT:160', 'PUMP:UT:170', 'PUMP:UT:180', 'PUMP:UT:190',
                            'PUMP:UT:200', 'PUMP:UT:210', 'PUMP:UT:220', 'PUMPHTR:200']
        self.assertEqual(Targest2.childless, expected_output)

if __name__ == '__main__':
    unittest.main()
