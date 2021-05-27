class RoleModel:
    def __init__(self, role_id, role_name="", can_role=False, can_user=False, can_production=False, can_packing=False,
                 can_inspection=False, can_inoculation=False, can_production_in_charge=False,
                 can_production_reviewer=False,can_packing_in_charge=False,
                 can_packing_reviewer=False,can_inspection_in_charge=False,
                 can_inspection_reviewer=False):
        self.role_id = role_id
        self.role_name = role_name
        self.can_role = can_role
        self.can_user = can_user
        self.can_production = can_production
        self.can_packing = can_packing
        self.can_inspection = can_inspection
        self.can_inoculation = can_inoculation
        self.can_production_in_charge = can_production_in_charge
        self.can_production_reviewer = can_production_reviewer
        self.can_packing_in_charge = can_packing_in_charge
        self.can_packing_reviewer = can_packing_reviewer
        self.can_inspection_in_charge = can_inspection_in_charge
        self.can_inspection_reviewer = can_inspection_reviewer
