def get_mock_response(message: str, current_transaction: str | None):

    normalised_message = message.lower()

    if "reversal" in normalised_message:
        return {
            "type": "policy_answer",
            "answer": (
                "Failed payments are normally reversed "
                "within 3–5 business days."
            ),
            "citations": [
                {
                    "title": "Failed Payment Policy",
                    "section": "Reversal Timeline"
                }
            ]
        }

    
    if "txn-1002" in normalized_message:
        return {
            "type": "transaction_status",
            "answer": (
                "TXN-****002 has FAILED. "
                "Reason: BANK_DECLINED."
            ),
            "current_transaction": "TXN-1002"
        }

    if "ticket" in normalized_message:
        if current_transaction is None:
            return {
                "type": "clarification",
                "answer": (
                    "Which transaction should I create "
                    "the ticket for?"
                )
            }

        return {
            "type": "proposed_action",
            "proposed_action": {
                "action": "CREATE_SUPPORT_TICKET",
                "transaction_id": current_transaction,
                "masked_transaction_id": "TXN-****002",
                "issue": "Failed payment reversal"
            }
        }

    return {
        "type": "unsupported",
        "answer": (
            "I can help with payment policies, transaction "
            "status and support-ticket creation."
        )
    }
