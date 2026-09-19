import streamlit as st

st.title("ResolveAI")
st.caption("Payment Support Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "proposed_action" not in st.session_state:
    st.session_state.proposed_action = None


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_message = st.chat_input("Ask about a payment")

if user_message:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    message = user_message.lower()

    if "reversal" in message:
        response = "Failed payments are normally reversed within 3-5 business days."

        st.session_state.messages.append(
            {
            "role": "assistant",
            "content": response
        }
        )

        st.session_state["citation"] = {
            "title": "Failed Payment Policy",
            "section": "Reversal Timeline"
        }

    elif "txn-1002" in message:
        response = "TXN-****002 has FAILED. Reason: BANK_DECLINED."

        st.session_state.message.append(
            {
                "role": "assistant",
                "content": response
            }
        )
        st.session_state.current_transaction = "TXN-1002"

    elif "create" in message and "ticket" in message:
        st.session_state.proposed_action = {
            "transaction_id": st.session_state.get(
                "current_transaction",
                "TXN-1002"
            ),
            "issue": "Failed payment reversal"
        }
    else:

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "I can help with payment policies and transaction status."
            }
        
        )
    st.rerun()



if "citatation" in st.session_state:
    citatation = st.session_state.citation


    with st.expander("View Source"):
        st.write(f"Policy: {citation['title']}")
        st.write(f"Section: {citation['section']}")


if st.session_state.proposed_action:
    action = st.session_state.proposed_action

    st.warning("Approval required")
    st.write(f"Transaction: {action['transaction_id']}")
    st.write(f"Issue: {action['issue']}")

     approve, edit, cancel = st.columns(3)

     with approve:
        if st.button("Approve"):
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Ticket TKT-5001 was created successfully."
            })
            st.session_state.proposed_action = None
            st.rerun()

    with edit:
        if st.button("Edit"):
            st.session_state.editing = True

    with cancel:
        if st.button("Cancel"):
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Ticket creation was cancelled."
            })
            st.session_state.proposed_action = None
            st.rerun()








