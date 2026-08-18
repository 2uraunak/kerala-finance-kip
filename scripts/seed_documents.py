"""
Seed sample Kerala Finance Department documents for demonstration.
Creates realistic mock PDFs with actual-style content.
"""
import os
import sys
import uuid
import json
from datetime import datetime

# Mock document metadata for Kerala Finance GOs
SAMPLE_DOCUMENTS = [
    {
        "id": str(uuid.uuid4()),
        "title": "GO(Ms) No.45/2023/Fin — Revision of Dearness Allowance for State Government Employees",
        "doc_number": "GO(Ms)No.45/2023/Fin",
        "doc_type": "government_order",
        "status": "superseded",
        "year": 2023,
        "issue_date": "2023-01-01",
        "is_scanned": False,
        "is_restricted": False,
        "tags": ["dearness allowance", "salary revision", "state employees"],
        "raw_text": """GOVERNMENT OF KERALA
Finance (Pay) Department

G.O.(Ms) No.45/2023/Fin                                          Dated: 01/01/2023

Subject: Revision of Dearness Allowance to State Government employees — with effect from 01.01.2023.

Read:
(1) G.O.(Ms.) No.234/2022/Fin dated 01.07.2022
(2) G.O.(Ms.) No.156/2022/Fin dated 01.01.2022

ORDER

The Government of Kerala is pleased to sanction revision of Dearness Allowance
to State Government employees as follows:

1. The Dearness Allowance payable to State Government employees shall be
   enhanced from 34% to 38% of basic pay with effect from 01.01.2023.

2. The arrears of DA for the period 01.01.2023 shall be credited to the
   General Provident Fund Account of the employees concerned.

3. The revised DA shall be paid in cash from the month of March 2023.

4. This order will apply to:
   (a) All State Government servants
   (b) Employees of Government-aided institutions
   (c) Pensioners (proportionate DA)

5. Financial implication: ₹ 450 Crore per annum approximately.

By order of the Governor
SECRETARY TO GOVERNMENT""",
        "summary": "Revision of DA from 34% to 38% for Kerala state employees effective 01.01.2023. Financial implication: ₹450 Crore/year.",
    },
    {
        "id": str(uuid.uuid4()),
        "title": "GO(Ms) No.112/2023/Fin — Revision of Dearness Allowance (Superseding GO 45/2023)",
        "doc_number": "GO(Ms)No.112/2023/Fin",
        "doc_type": "government_order",
        "status": "active",
        "year": 2023,
        "issue_date": "2023-07-01",
        "is_scanned": False,
        "is_restricted": False,
        "tags": ["dearness allowance", "salary revision", "state employees"],
        "raw_text": """GOVERNMENT OF KERALA
Finance (Pay) Department

G.O.(Ms) No.112/2023/Fin                                         Dated: 01/07/2023

Subject: Revision of Dearness Allowance to State Government employees — with effect from 01.07.2023.

Read:
(1) G.O.(Ms.) No.45/2023/Fin dated 01.01.2023 (Superseded)

ORDER

The Government of Kerala is pleased to sanction further revision of Dearness Allowance:

1. The Dearness Allowance payable to State Government employees shall be
   enhanced from 38% to 42% of basic pay with effect from 01.07.2023.

2. G.O.(Ms.) No.45/2023/Fin dated 01.01.2023 stands superseded to this extent.

3. Financial implication: ₹ 520 Crore per annum approximately.

By order of the Governor
SECRETARY TO GOVERNMENT""",
        "summary": "Revision of DA from 38% to 42% for Kerala state employees effective 01.07.2023. Supersedes GO 45/2023.",
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Kerala Budget 2024-25 — Finance Department Allocation and Key Provisions",
        "doc_number": "Budget_2024_25",
        "doc_type": "budget",
        "status": "active",
        "year": 2024,
        "issue_date": "2024-02-01",
        "is_scanned": False,
        "is_restricted": False,
        "tags": ["budget", "2024-25", "allocation", "capital expenditure"],
        "raw_text": """KERALA STATE BUDGET 2024-25
Finance Department

BUDGET HIGHLIGHTS

Total Budget Size: ₹ 2,23,979 Crore

KEY ALLOCATIONS:
1. Education: ₹ 38,421 Crore (17.15% of budget)
2. Health: ₹ 11,234 Crore (5.01%)
3. Infrastructure: ₹ 22,456 Crore (10.02%)
4. Social Welfare: ₹ 18,234 Crore (8.14%)
5. Agriculture: ₹ 4,567 Crore (2.04%)

FISCAL INDICATORS:
- Revenue Deficit: ₹ 12,345 Crore
- Capital Expenditure: ₹ 45,678 Crore
- State's Own Tax Revenue: ₹ 89,234 Crore
- GST Revenue: ₹ 45,123 Crore (50.57% of SOTR)

IMPORTANT PROVISIONS:
Para 45: The government proposes to enhance the social security pension from ₹1,600 to ₹1,800 per month.
Para 78: A new scheme 'Kerala Fibre Optic Network Phase 2' allocated ₹ 2,345 Crore.
Para 112: GST compliance improvement measures — target 95% filing rate by March 2025.""",
        "summary": "Kerala Budget 2024-25 with total outlay of ₹2,23,979 Crore. Key highlights: Education ₹38,421 Cr, Infrastructure ₹22,456 Cr, GST revenue ₹45,123 Cr.",
    },
    {
        "id": str(uuid.uuid4()),
        "title": "GST Circular No.178/10/2024 — Clarification on Works Contract Services for Government",
        "doc_number": "GST_Circular_178_2024",
        "doc_type": "gst_policy",
        "status": "active",
        "year": 2024,
        "issue_date": "2024-03-15",
        "is_scanned": False,
        "is_restricted": False,
        "tags": ["GST", "works contract", "government", "circular"],
        "raw_text": """CIRCULAR No. 178/10/2024-GST

F.No. CBIC-20001/7/2024-GST
Government of India
Ministry of Finance
Department of Revenue
Central Board of Indirect Taxes and Customs

Dated: 15th March, 2024

Subject: Clarification regarding applicability of GST on services provided by Government entities.

1. References have been received from various trade and industry seeking clarification on
   the applicability of GST on works contract services provided to Government entities.

2. The matter has been examined and it is hereby clarified as follows:

   2.1 Works contract services provided to Central/State Government, Union Territories or
       Local authorities involving construction of roads, bridges, railways, waterways shall
       attract GST at the rate of 12%.

   2.2 Works contract services other than those mentioned at 2.1 above shall attract GST
       at the rate of 18%.

   2.3 Pure services (excluding works contract) to Government shall attract Nil GST if
       covered under Notification 12/2017-CT(R).

3. HSN Code 9954 applies to construction services.
   HSN Code 9997 applies to other services to Government.

4. This circular supersedes all previous clarifications on this subject.

By order and in the name of the President of India
(Joint Secretary to Government of India)""",
        "summary": "GST clarification: works contract for roads/bridges/railways to government attracts 12% GST; others 18%. Pure services under Notification 12/2017-CT(R) attract Nil GST.",
    },
    {
        "id": str(uuid.uuid4()),
        "title": "CLASSIFIED: Finance Department Internal Audit Report Q3 2024",
        "doc_number": "AUDIT_Q3_2024_RESTRICTED",
        "doc_type": "other",
        "status": "active",
        "year": 2024,
        "issue_date": "2024-10-01",
        "is_scanned": False,
        "is_restricted": True,  # RESTRICTED — Admin only
        "tags": ["audit", "restricted", "internal"],
        "raw_text": """RESTRICTED — FOR AUTHORIZED PERSONNEL ONLY

FINANCE DEPARTMENT INTERNAL AUDIT REPORT
Q3 2024 (July — September 2024)

[This document contains sensitive financial audit findings and is restricted
to authorized Finance Department personnel only.]

AUDIT FINDINGS SUMMARY:
1. Overall compliance rate: 87.3%
2. Pending reconciliations: ₹ 234 Crore
3. High-risk transactions identified: 12

NOTE: This document is accessible only to Admin-level users in the KIP system.""",
        "summary": "[RESTRICTED] Internal audit report Q3 2024. Accessible to Admin only.",
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Office Memorandum — Austerity Measures for 2024-25",
        "doc_number": "OM_Finance_2024_Austerity",
        "doc_type": "office_memorandum",
        "status": "active",
        "year": 2024,
        "issue_date": "2024-04-01",
        "is_scanned": False,
        "is_restricted": False,
        "tags": ["austerity", "expenditure control", "2024-25"],
        "raw_text": """GOVERNMENT OF KERALA
Finance Department

No. 14/57/2024/Fin                                              Date: 01.04.2024

OFFICE MEMORANDUM

Sub: Austerity measures to be followed during 2024-25.

In continuation of the Government's policy of expenditure management, the following
austerity measures shall be strictly observed during 2024-25:

1. RESTRICTIONS ON EXPENDITURE:
   (a) No new posts shall be created without prior Finance Department concurrence.
   (b) All foreign tours must be pre-approved by the Chief Minister's Office.
   (c) Expenditure on vehicles shall not exceed 80% of the previous year's actual.
   (d) Purchase of new furniture/equipment above ₹5,000 requires Finance sanction.

2. PRIORITY SECTORS (exempt from austerity):
   (a) Healthcare and COVID-19 related expenditure
   (b) Infrastructure projects under KIIFB
   (c) Social welfare payments to beneficiaries

3. All departments shall submit monthly expenditure statements by the 5th of each month.

4. Non-compliance will be viewed seriously and the concerned DDO will be held responsible.

Principal Secretary (Finance)
Government of Kerala""",
        "summary": "Austerity measures for FY 2024-25: restrictions on new posts, foreign tours, vehicle expenditure. Healthcare and infrastructure exempt.",
    },
]


def seed_documents():
    """Insert mock documents directly into the database (bypassing ingestion for speed)."""
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker

    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://kip:kip_secret@localhost:5432/kipdb").replace(
        "postgresql+asyncpg://", "postgresql://"
    )
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    SessionLocal = sessionmaker(bind=engine)

    with SessionLocal() as session:
        for doc in SAMPLE_DOCUMENTS:
            existing = session.execute(
                text("SELECT id FROM documents WHERE doc_number=:dn"),
                {"dn": doc["doc_number"]}
            ).fetchone()
            if not existing:
                session.execute(text("""
                    INSERT INTO documents (
                        id, title, doc_number, doc_type, status, department, year,
                        issue_date, is_scanned, is_restricted, is_indexed, tags,
                        raw_text, summary, created_at, updated_at
                    ) VALUES (
                        :id, :title, :doc_number, :doc_type, :status,
                        'Finance Department, Kerala', :year, :issue_date,
                        :is_scanned, :is_restricted, true, :tags,
                        :raw_text, :summary, now(), now()
                    )
                """), {
                    **doc,
                    "tags": json.dumps(doc.get("tags", [])),
                    "issue_date": datetime.strptime(doc["issue_date"], "%Y-%m-%d"),
                })
                print(f"✅ Seeded: {doc['doc_number']} — {doc['title'][:60]}...")
            else:
                print(f"⏭️  Already exists: {doc['doc_number']}")

        # Set up lineage: GO 112 supersedes GO 45
        docs = {d["doc_number"]: d["id"] for d in SAMPLE_DOCUMENTS}
        old_id = docs.get("GO(Ms)No.45/2023/Fin")
        new_id = docs.get("GO(Ms)No.112/2023/Fin")
        if old_id and new_id:
            session.execute(text("""
                UPDATE documents SET superseded_by_id=:new_id WHERE id=:old_id
            """), {"new_id": new_id, "old_id": old_id})
            session.execute(text("""
                UPDATE documents SET supersedes_id=:old_id WHERE id=:new_id
            """), {"old_id": old_id, "new_id": new_id})
            print(f"\n🔗 Lineage set: GO 45/2023 superseded by GO 112/2023")

        session.commit()
    print("\n✅ Document seeding complete! 6 documents seeded (including 1 restricted).")


if __name__ == "__main__":
    seed_documents()
