from Constants import connString
import pyodbc
import time
class InspectionModel:
    def __init__(self, inspection_id, production_batch_no="", dosage_form="",
                 inspection_date_time=None,
                 specification="", inspection_standards="", inspection_equipments="", inspection_observations="",
                 inspection_calculations="", inspection_results="", inspection_in_charge="",
                 inspection_reviewer=""):
        self.inspection_id = inspection_id
        self.production_batch_no = production_batch_no
        self.dosage_form = dosage_form
        self.inspection_date_time = inspection_date_time
        self.specification = specification
        self.inspection_standards = inspection_standards
        self.inspection_equipments = inspection_equipments
        self.inspection_observations = inspection_observations
        self.inspection_calculations = inspection_calculations
        self.inspection_results = inspection_results
        self.inspection_in_charge = inspection_in_charge
        self.inspection_reviewer = inspection_reviewer

    @staticmethod
    def get_all_inspection():
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "SELECT * FROM InspectionDetails ORDER BY dosageForm"
        cursor.execute(sqlcmd1)
        records = []

        for dbrow in cursor.fetchall():

            row = InspectionModel(dbrow[0], dbrow[1], dbrow[2], dbrow[3], dbrow[4], dbrow[5], dbrow[6], dbrow[7],
                                  dbrow[8], dbrow[9], dbrow[10], dbrow[11])
            records.append(row)
        return records

    @staticmethod
    def get_inspection_by_id(inspection_id):
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "SELECT * FROM InspectionDetails WHERE inspectionID = ?"
        cursor.execute(sqlcmd1, inspection_id)
        record = None

        for dbrow in cursor.fetchall():
            print(dbrow[0], dbrow[1], dbrow[2], dbrow[3], str(dbrow[4])[0:16].replace(" ", "T"), dbrow[5], dbrow[6], dbrow[7],
                                  dbrow[8], dbrow[9], dbrow[10], dbrow[11])
            record = InspectionModel(dbrow[0], dbrow[1], dbrow[2], dbrow[3], dbrow[4], dbrow[5], dbrow[6], dbrow[7],
                                  dbrow[8], dbrow[9], dbrow[10], dbrow[11])
        return record

    @staticmethod
    def insert_inspection(inspection_obj):
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "INSERT INTO InspectionDetails (inspectionID, productionBatchNo, " \
                  "dosageForm, inspectionDateTime, specification, inspectionStandards," \
                  "inspectionEquipments, inspectionObservations, inspectionCalculations, inspectionResults, " \
                  "inspectionInCharge, inspectionReviewer) " \
                  "VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
        print((inspection_obj.inspection_id,                       inspection_obj.production_batch_no,
                       inspection_obj.dosage_form,                 inspection_obj.inspection_date_time,
                        inspection_obj.specification,              inspection_obj.inspection_standards,
                        inspection_obj.inspection_equipments,      inspection_obj.inspection_observations,
                        "inspection_obj.inspection_calculations",   "inspection_obj.investigationReport",
                        inspection_obj.inspection_in_charge,         inspection_obj.inspection_reviewer))
        cursor.execute(sqlcmd1, (inspection_obj.inspection_id,     inspection_obj.production_batch_no,
                       inspection_obj.dosage_form,                 inspection_obj.inspection_date_time,
                        inspection_obj.specification,              inspection_obj.inspection_standards,
                        inspection_obj.inspection_equipments,      inspection_obj.inspection_observations,
                        inspection_obj.inspection_calculations,    inspection_obj.inspection_results,
                        inspection_obj.inspection_in_charge,         inspection_obj.inspection_reviewer))

    @staticmethod
    def update_inspection(inspection_obj):
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "UPDATE InspectionDetails SET productionBatchNo = ?, dosageForm = ?, " \
                  "inspectionDateTime = ?, specification = ?, inspectionStandards = ?," \
                  "inspectionEquipments = ?, inspectionObservations = ?," \
                  "  inspectionCalculations = ?, inspectionResults=?, inspectionInCharge= ?, inspectionReviewer=?" \
                  " WHERE inspectionID = ?"
        cursor.execute(sqlcmd1,  (inspection_obj.production_batch_no,
                       inspection_obj.dosage_form,
                       inspection_obj.inspection_date_time, inspection_obj.specification,
                       inspection_obj.inspection_standards, inspection_obj.inspection_equipments,
                       inspection_obj.inspection_observations, inspection_obj.inspection_calculations,
                       inspection_obj.inspection_results,
                       inspection_obj.inspection_in_charge, inspection_obj.inspection_reviewer,
                       inspection_obj.inspection_id))

    @staticmethod
    def delete_inspection(inspection_obj):
        conn = pyodbc.connect(connString, autocommit=True)
        cursor = conn.cursor()
        sqlcmd1 = "DELETE FROM InspectionDetails WHERE inspectionID = ?"
        cursor.execute(sqlcmd1, (inspection_obj.inspection_id))

