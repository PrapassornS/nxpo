*คำอธิบาย:

1. ตั้งค่าเริ่มต้น rfq_state เป็น draft
2. แก้ไขฟังค์ชั่น action_convert_to_order เมื่อสร้าง purchase order ให้เป็นสถานะ draft และ
   rfq ที่ถูกเลือกไป convert to po ให้ rfq_state เป็น done และที่เหลือเป็น cancel
