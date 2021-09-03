"""
Defines various methods used to execute queries on db

Authored by Jon Dong 8/27/21
"""
def insert_row_into_manual_review(tblname, rowid, colname, reason, db_cur, db_con):
    """
        Inserts a row into manual review table
    :param tblname: tblename where error occurred (mgbedew_ethnicity)
    :param rowid:   rowid where error occurred
    :param colname: colname of ethnicity
    :param reason:  reason for error
    :param db_cur: DB cursor
    :param db_con: DB connection

    """
    db_cur.execute('Insert into manual_review (tbl_name, col_name, rowid, reason) VALUES  (%s, %s, %s, %s)',
                   (tblname, rowid, colname, reason)
                   )
    db_con.commit()

def insert_row_into_parsed_patientidentifiers(id, epicpmrn,empi, bwh, mgh , db_cur, db_con):
    """
    Inserts row into parsed table
    :param id: rowid
    :param empi:  empi
    :param epicpmrn: epicpmrn
    :param bwh: bwh id
    :param mgh: mgh id
    :param db_cur: DB Cursor
    :param db_con: DB Connection
    :return:
    """
    db_cur.execute('Insert into dev_parsed_ethnicity (empi,epic_pmrn, ethnicity, ethnicity_detail, mgbedw_source_id) VALUES  (%s, %s, %s, %s)',
                   ( epicpmrn, empi, bwh, mgh)
                   )
    db_con.commit()


def grab_info_from_mgbdew_patientidentifiers(rownum, db_cur, db_con):
    """
    grabs info from the mgbdew ethnicity table and returns epicpmrn, empi bwh and mgh
    :param rownum: rownum to select info from
    :param db_cur: DB Cursor
    :param db_con: DB Connection
    :return: returns epicpmrn, empi bwh and mgh
    """
    db_cur.execute('SELECT epic_pmrn,empi, bwh, mgh FROM mgbedw_patientidentifiers where id = %s', (rownum,))
    db_con.commit()
    result = db_cur.fetchone()
    return(result[0],result[1], result[2], result[3])